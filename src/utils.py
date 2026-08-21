"""Utility functions for fetching and parsing."""
import httpx
from typing import Optional


async def fetch_page(url: str, headers: Optional[dict] = None, timeout: int = 30) -> Optional[str]:
    """
    Fetch a page using httpx.
    
    Args:
        url: URL to fetch
        headers: Optional request headers
        timeout: Request timeout in seconds
        
    Returns:
        HTML content or None on failure
    """
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=timeout) as client:
            response = await client.get(url, headers=headers)
            
            if response.status_code != 200:
                print(f'❌ HTTP {response.status_code} for {url}')
                return None
                
            if len(response.text) < 500:
                print(f'⚠️ Response too small ({len(response.text)} bytes) for {url}')
                return None
                
            return response.text
            
    except Exception as e:
        print(f'❌ Error fetching {url}: {e}')
        return None
