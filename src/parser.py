"""Parser functions for extracting job data."""
from bs4 import BeautifulSoup
from typing import Dict, List, Optional
import re


def extract_job_links(html: str) -> List[str]:
    """
    Extract job position links from the jobs listing page.
    
    Args:
        html: HTML content of the jobs page
        
    Returns:
        List of job URLs
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    # Find all links with /jobs/position/ in href
    for a in soup.find_all('a', href=True):
        href = a.get('href', '')
        if '/jobs/position/' in href:
            # Convert relative URLs to absolute
            if href.startswith('/'):
                href = f'https://employmenthero.com{href}'
            elif not href.startswith('http'):
                href = f'https://employmenthero.com/jobs/position/{href}'
                
            # Avoid duplicates
            if href not in links:
                links.append(href)
    
    return links


def parse_job_detail(html: str, url: str) -> Optional[Dict[str, str]]:
    """
    Parse job details from a job detail page.
    
    Args:
        html: HTML content of the job detail page
        url: URL of the job posting
        
    Returns:
        Dictionary with job data or None on failure
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    try:
        # Extract job title (usually in h1)
        title_elem = soup.find('h1')
        job_title = title_elem.get_text(strip=True) if title_elem else None
        
        # Extract company name (look for "at [company]" pattern or h2)
        company = None
        for elem in soup.find_all(['a', 'h2', 'span', 'div']):
            text = elem.get_text(strip=True)
            if text.startswith('at '):
                company = text[3:].strip()
                break
            # Also check class names
            classes = ' '.join(elem.get('class', [])).lower()
            if 'company' in classes and text:
                company = text
                break
        
        if not company:
            # Fallback: look in breadcrumbs or after title
            h2 = soup.find('h2')
            if h2:
                company = h2.get_text(strip=True)
        
        # Extract location
        location = None
        for elem in soup.find_all(['span', 'div', 'p']):
            text = elem.get_text(strip=True)
            # Look for patterns like "City, State" or elements with location in class
            if any(suburb in text for suburb in ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide', 'Perth', 'Victoria', 'NSW', 'QLD']):
                # Clean up the location text
                if '•' in text:
                    parts = text.split('•')
                    for part in parts:
                        if any(s in part for s in ['Sydney', 'Melbourne', 'Brisbane', 'Victoria', 'NSW']):
                            location = part.strip()
                            break
                else:
                    location = text
                break
        
        # Extract salary
        salary = None
        for elem in soup.find_all(['span', 'div', 'p']):
            text = elem.get_text(strip=True)
            # Look for dollar signs or salary keywords
            if '$' in text or 'salary' in text.lower():
                # Extract just the salary part
                salary_match = re.search(r'\$[\d,]+(?:\s*-\s*\$[\d,]+)?(?:\s+(?:per|/)\s+\w+)?', text)
                if salary_match:
                    salary = salary_match.group(0)
                else:
                    salary = text
                break
        
        # Extract job type (Full-time, Part-time, Casual, etc.)
        job_type = None
        for elem in soup.find_all(['span', 'div']):
            text = elem.get_text(strip=True)
            if re.search(r'\b(full[- ]time|part[- ]time|casual|temporary|contract|permanent)\b', text, re.IGNORECASE):
                job_type = re.search(r'\b(full[- ]time|part[- ]time|casual|temporary|contract|permanent)\b', text, re.IGNORECASE).group(0)
                break
        
        # Extract description
        description = None
        # Look for common description containers
        for selector in [
            soup.find('div', class_=re.compile(r'description', re.I)),
            soup.find('div', class_=re.compile(r'content', re.I)),
            soup.find('section', class_=re.compile(r'description', re.I))
        ]:
            if selector:
                description = selector.get_text(separator=' ', strip=True)
                break
        
        # Fallback: get all paragraph text
        if not description:
            paragraphs = soup.find_all('p')
            if paragraphs:
                description = ' '.join([p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 50])
        
        # Truncate description if too long
        if description and len(description) > 5000:
            description = description[:5000] + '...'
        
        return {
            'jobTitle': job_title,
            'company': company,
            'location': location,
            'salary': salary,
            'jobType': job_type,
            'description': description,
            'url': url
        }
        
    except Exception as e:
        print(f'❌ Error parsing job detail: {e}')
        return None
