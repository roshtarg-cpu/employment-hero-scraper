# 🇦🇺 Employment Hero Job Scraper

[![Apify](https://img.shields.io/badge/Apify-Actor-00D4AA?style=for-the-badge&logo=apify)](https://apify.com/fervent_bus/employment-hero-scraper)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![AI Agents](https://img.shields.io/badge/AI_Agents-Compatible-FF6B6B?style=for-the-badge&logo=openai)](https://github.com/roshtarg-cpu/employment-hero-scraper)
[![MCP](https://img.shields.io/badge/MCP-Ready-4ECDC4?style=for-the-badge)](https://apify.com/integrations)

> 🚀 **First-mover advantage:** Only 5 competing actors on Apify for Employment Hero  
> 🤖 **AI-Ready:** Works seamlessly with Claude Code, ChatGPT, and other AI assistants via Apify MCP  
> 🎯 **Australian Market:** Extract jobs from Australia's leading employment platform

---

## ✨ Features

- 🔍 **Smart Search** — Filter by job title, location, and keywords
- 📊 **Rich Data** — Extract titles, companies, locations, salaries, descriptions, job types
- 🏎️ **Fast & Reliable** — Uses JSON-LD structured data for accurate extraction
- 🤖 **AI-First Design** — Built for Claude Code, ChatGPT, and recruitment automation
- 🌏 **Australian Focus** — Covers jobs across Sydney, Melbourne, Brisbane, and all major cities
- 💰 **Cost-Effective** — $0.005 per job + $0.05 start fee

---

## 🤖 AI Agent Use Cases

Perfect for AI assistants and automation workflows:

### 🔹 **Recruitment Automation**
```
"Find 50 software engineering jobs in Sydney on Employment Hero"
→ AI agent scrapes and filters relevant positions
→ Builds shortlist with salary data and job descriptions
```

### 🔹 **Job Market Research**
```
"Compare salaries for data scientist roles across Melbourne and Brisbane"
→ Extracts salary ranges from Employment Hero listings
→ Analyzes market trends by location
```

### 🔹 **Candidate Matching**
```
"Get all part-time marketing jobs in Adelaide with descriptions"
→ Scrapes job details including requirements
→ Matches candidates to opportunities
```

### 🔹 **Competitive Intelligence**
```
"Monitor new job postings from [Company X]"
→ Track hiring patterns and expansion signals
→ Alert when competitor posts new roles
```

---

## 📥 Input Configuration

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `searchQuery` | String | Job title or keyword | `"software engineer"` |
| `location` | String | City or state filter | `"Sydney"`, `"Victoria"` |
| `maxResults` | Integer | Max jobs to scrape (1-500) | `50` |
| `proxyConfiguration` | Object | Apify proxy settings | `{"useApifyProxy": true}` |

### Example Input
```json
{
  "searchQuery": "data analyst",
  "location": "Melbourne",
  "maxResults": 100
}
```

---

## 📤 Output Schema

Each job listing includes:

```json
{
  "jobTitle": "Senior Data Analyst",
  "company": "Tech Solutions Australia",
  "location": "Melbourne, Victoria, 3000",
  "salary": "$90,000 - $110,000",
  "jobType": "FULL_TIME",
  "description": "We're seeking an experienced data analyst to join our analytics team...",
  "url": "https://employmenthero.com/jobs/position/...",
  "scrapedAt": "2026-08-22T02:55:00.000Z"
}
```

### Field Descriptions

- **jobTitle** — Job position title
- **company** — Hiring organization name
- **location** — Full address (suburb, state, postcode)
- **salary** — Salary range (if available)
- **jobType** — Employment type (FULL_TIME, PART_TIME, CASUAL, etc.)
- **description** — Clean job description (HTML removed)
- **url** — Direct link to job posting
- **scrapedAt** — ISO timestamp of data extraction

---

## 🚀 Quick Start

### Via Apify Console
1. Open the [actor page](https://apify.com/fervent_bus/employment-hero-scraper)
2. Configure input (search query, location, max results)
3. Click **Start** and download results as JSON, CSV, or Excel

### Via Apify API
```bash
curl -X POST "https://api.apify.com/v2/acts/fervent_bus~employment-hero-scraper/runs" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "searchQuery": "software engineer",
    "location": "Sydney",
    "maxResults": 50
  }'
```

### Via Python (Apify Client)
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_API_TOKEN")

run = client.actor("fervent_bus/employment-hero-scraper").call(
    run_input={
        "searchQuery": "product manager",
        "location": "Brisbane",
        "maxResults": 100
    }
)

# Fetch results
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"{item['jobTitle']} at {item['company']} - {item['location']}")
```

### Via JavaScript (Apify Client)
```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_API_TOKEN' });

const run = await client.actor('fervent_bus/employment-hero-scraper').call({
  searchQuery: 'marketing manager',
  location: 'Sydney',
  maxResults: 50
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.forEach(job => {
  console.log(`${job.jobTitle} - ${job.company} (${job.location})`);
});
```

---

## 🤖 Claude Code / ChatGPT Integration

This actor is **optimized for AI assistants** via [Apify MCP (Model Context Protocol)](https://apify.com/integrations).

### Example Prompts for AI Agents

**Claude Code:**
```
Use Employment Hero scraper to find 100 tech jobs in Sydney. 
Filter for roles with "Python" in the description and salary > $100k.
Export to CSV.
```

**ChatGPT + Apify:**
```
Scrape Employment Hero for remote marketing jobs across Australia. 
Compare locations by number of openings and average salary.
```

**Custom AI Workflow:**
```python
# In your AI agent code
from apify_client import ApifyClient

def search_jobs(query, location, count=50):
    """AI-callable function to search Employment Hero"""
    client = ApifyClient(os.getenv("APIFY_TOKEN"))
    run = client.actor("fervent_bus/employment-hero-scraper").call({
        "searchQuery": query,
        "location": location,
        "maxResults": count
    })
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())
```

---

## 🎯 Who Is This For?

- **🤖 AI Developers** — Build recruitment bots, job aggregators, salary analyzers
- **📈 HR Teams** — Automate job market research and competitor tracking
- **💼 Recruiters** — Monitor new openings, track hiring trends
- **📊 Data Analysts** — Research employment market trends across Australia
- **🔧 Job Boards** — Aggregate Employment Hero listings into your platform

---

## 🛠️ Technical Details

- **Technology:** Python 3.11 + httpx + BeautifulSoup4
- **Data Source:** JSON-LD structured data (schema.org JobPosting)
- **Protection:** None required (clean server-rendered HTML)
- **Speed:** ~100 jobs per minute
- **Memory:** 1024 MB recommended
- **Proxy:** Optional (included in Apify subscription)

---

## 💰 Pricing

| Event | Price | Description |
|-------|-------|-------------|
| **Job Scraped** | $0.005 | Per job listing extracted |
| **Actor Start** | $0.05 | One-time fee per run |

**Example cost:**
- 100 jobs = $0.05 + (100 × $0.005) = **$0.55 total**
- 500 jobs = $0.05 + (500 × $0.005) = **$2.55 total**

---

## 📚 Additional Resources

- 📖 [Actor Source Code](https://github.com/roshtarg-cpu/employment-hero-scraper)
- 🐛 [Report Issues](https://github.com/roshtarg-cpu/employment-hero-scraper/issues)
- 💬 [Apify Platform Documentation](https://docs.apify.com)
- 🤖 [Apify MCP Integration Guide](https://apify.com/integrations)

---

## 🔗 Related Actors

- **Seek Scraper** — Australia's largest job board
- **Indeed Australia** — International job listings
- **LinkedIn Jobs** — Professional network positions

---

## 📄 License

This actor is provided as-is under the MIT License.

---

## 🚀 Get Started Now

[![Run on Apify](https://img.shields.io/badge/Run_on-Apify-00D4AA?style=for-the-badge&logo=apify)](https://apify.com/fervent_bus/employment-hero-scraper)

**Compatible with Claude Code, ChatGPT, and AI agents via Apify MCP.**

---

Made with ❤️ for the AI automation community
