"""Main actor logic for Employment Hero job scraper."""
import asyncio
from datetime import datetime
from apify import Actor
from .utils import fetch_page
from .parser import extract_job_links, parse_job_detail


async def main():
    """Main actor entry point."""
    async with Actor:
        # Get input
        actor_input = await Actor.get_input() or {}
        search_query = actor_input.get('searchQuery', '').strip()
        location = actor_input.get('location', '').strip()
        max_results = actor_input.get('maxResults', 50)
        
        Actor.log.info(f'Starting Employment Hero scraper')
        Actor.log.info(f'Search query: {search_query or "all jobs"}')
        Actor.log.info(f'Location: {location or "all locations"}')
        Actor.log.info(f'Max results: {max_results}')
        
        # Build search URL
        base_url = 'https://employmenthero.com/jobs/'
        search_url = base_url
        
        # Add search parameters if provided
        params = []
        if search_query:
            params.append(f'q={search_query.replace(" ", "+")}')
        if location:
            params.append(f'location={location.replace(" ", "+")}')
        
        if params:
            search_url = f'{base_url}?{"&".join(params)}'
        
        Actor.log.info(f'Fetching job listings from: {search_url}')
        
        # Fetch the jobs listing page
        html = await fetch_page(search_url)
        
        if not html:
            Actor.log.error('Failed to fetch jobs listing page')
            return
        
        # Extract job links
        job_links = extract_job_links(html)
        Actor.log.info(f'Found {len(job_links)} job links')
        
        if not job_links:
            Actor.log.warning('No job links found on the page')
            return
        
        # Limit to maxResults
        job_links = job_links[:max_results]
        Actor.log.info(f'Processing {len(job_links)} jobs (limited to maxResults)')
        
        # Process each job
        scraped_count = 0
        failed_count = 0
        
        for i, job_url in enumerate(job_links, 1):
            try:
                Actor.log.info(f'[{i}/{len(job_links)}] Scraping: {job_url}')
                
                # Fetch job detail page
                job_html = await fetch_page(job_url)
                
                if not job_html:
                    Actor.log.warning(f'Failed to fetch job page: {job_url}')
                    failed_count += 1
                    continue
                
                # Parse job details
                job_data = parse_job_detail(job_html, job_url)
                
                if not job_data:
                    Actor.log.warning(f'Failed to parse job data: {job_url}')
                    failed_count += 1
                    continue
                
                # Add timestamp
                job_data['scrapedAt'] = datetime.utcnow().isoformat() + 'Z'
                
                # Handle missing fields (set to null instead of crashing)
                for field in ['jobTitle', 'company', 'location', 'salary', 'jobType', 'description']:
                    if not job_data.get(field):
                        job_data[field] = None
                
                # Push to dataset
                await Actor.push_data(job_data)
                scraped_count += 1
                
                # Log progress every 10 results
                if scraped_count % 10 == 0:
                    Actor.log.info(f'✅ Progress: {scraped_count} jobs scraped')
                
                # Small delay to be respectful
                await asyncio.sleep(1)
                
            except Exception as e:
                Actor.log.error(f'Error processing {job_url}: {e}')
                failed_count += 1
                continue
        
        # Final summary
        Actor.log.info('=== Scraping Complete ===')
        Actor.log.info(f'✅ Successfully scraped: {scraped_count} jobs')
        Actor.log.info(f'❌ Failed: {failed_count} jobs')
        Actor.log.info(f'📊 Total processed: {len(job_links)} jobs')
        
        # CRITICAL: Save task context for debugging and recovery
        await Actor.set_value('SAVED-TASK', {
            'actorId': Actor.get_env().get('actor_id'),
            'actorRunId': Actor.get_env().get('actor_run_id'),
            'defaultDatasetId': Actor.get_env().get('default_dataset_id'),
            'startedAt': Actor.get_env().get('started_at'),
            'input': actor_input,
            'stats': {
                'itemsScraped': scraped_count,
                'itemsFailed': failed_count,
                'totalProcessed': len(job_links),
                'searchQuery': search_query or 'all jobs',
                'location': location or 'all locations',
                'maxResults': max_results
            }
        })
        
        Actor.log.info('💾 Task context saved to SAVED-TASK')
