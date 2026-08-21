# Employment Hero Jobs Scraper

Extract job listings from Employment Hero's Australian job board (employmenthero.com/jobs/). Returns structured data including job title, company, location, salary, job type, and full descriptions.

## 🤖 AI Agent Compatible

This actor is optimized for AI agents including:
- **Claude** (via Anthropic MCP)
- **ChatGPT** (via OpenAI plugins)
- **Custom AI agents** using Apify MCP integration

Works seamlessly with conversational AI workflows for job market research, candidate sourcing, and recruitment automation.

## 📊 What Data You Get

Each job listing includes:
- **Job Title** - Position name
- **Company** - Employer name
- **Location** - City and state in Australia
- **Salary** - Pay range or rate (when available)
- **Job Type** - Full-time, Part-time, Casual, Contract, etc.
- **Description** - Full job description and requirements
- **URL** - Direct link to the job posting
- **Scraped At** - Timestamp of data collection

## 🎯 Who It's For

- **Recruiters** - Source candidates from Australian job market
- **Job Seekers** - Monitor opportunities matching your skills
- **Market Researchers** - Analyze employment trends and salary data
- **HR Teams** - Competitive intelligence and market benchmarking
- **Data Analysts** - Build datasets for workforce analytics

## 💡 Example Use Cases

### With Claude AI
```
"Find all software engineer jobs in Sydney from Employment Hero 
and create a comparison table with salary ranges"
```

### With ChatGPT
```
"Scrape remote marketing jobs from Employment Hero and summarize 
the most common requirements"
```

### Programmatic Access
```python
from apify_client import ApifyClient

client = ApifyClient('YOUR_API_TOKEN')
run = client.actor('fervent_bus/employment-hero-scraper').call(
    run_input={
        'searchQuery': 'data analyst',
        'location': 'Melbourne',
        'maxResults': 20
    }
)

for item in client.dataset(run['defaultDatasetId']).iterate_items():
    print(f"{item['jobTitle']} at {item['company']} - {item['location']}")
```

## 🔧 Input Configuration

```json
{
  "searchQuery": "software engineer",
  "location": "Sydney",
  "maxResults": 10
}
```

### Input Fields

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `searchQuery` | string | Job title or keyword to search for | `"software engineer"` |
| `location` | string | City or state to filter jobs | `"Sydney"` |
| `maxResults` | integer | Maximum number of jobs to scrape (1-500) | `50` |

## 📤 Example Output

```json
{
  "jobTitle": "Senior Software Engineer",
  "company": "Tech Company Australia",
  "location": "Sydney, NSW",
  "salary": "$120,000 - $150,000 per year",
  "jobType": "Full-time",
  "description": "We are seeking an experienced Senior Software Engineer to join our growing team...",
  "url": "https://employmenthero.com/jobs/position/tech-company-senior-software-engineer-abc123/",
  "scrapedAt": "2026-08-21T12:34:56.789Z"
}
```

## 🚀 Features

- ✅ **No JavaScript rendering** - Fast httpx + BeautifulSoup extraction
- ✅ **No bot protection** - Clean, server-rendered HTML
- ✅ **Structured output** - Consistent JSON schema
- ✅ **Null-safe** - Gracefully handles missing fields
- ✅ **Rate-limited** - Respectful 1-second delay between requests
- ✅ **Progress logging** - Real-time scraping status
- ✅ **Error recovery** - Continues on individual failures

## 🏷️ Tags

`jobs` `employment` `recruitment` `australia` `hiring` `careers` `job-board` `scraper` `ai-agent` `mcp` `claude` `chatgpt`

## 📝 Notes

- Employment Hero is Australia's leading HR and payroll platform
- Job listings cover all industries and experience levels
- Data freshness depends on when employers post/update listings
- Some jobs may not include salary information
- Respects robots.txt and uses reasonable rate limiting

## 🔗 Links

- [Employment Hero Jobs](https://employmenthero.com/jobs/)
- [Apify Platform](https://apify.com/)
- [Apify MCP Integration](https://apify.com/integrations/mcp)

---

**Built for AI agents** | Compatible with Claude, ChatGPT & custom MCP clients
