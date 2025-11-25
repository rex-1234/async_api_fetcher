import aiohttp
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential
from utils import logger

TIMEOUT = 5 # seconds

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
async def fetch_url(session, url):
    """Fetch data from url with retries using aiohttp."""
    try:
        logger.info(f"Fetching URL: {url}")

        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.text()

            logger.info(f"Successfully fetched data from {url}")
            return {'url': url, 'data': data}

    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        raise

async def fetch_all(urls):
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=TIMEOUT)) as session:
        results = []

        async with asyncio.TaskGroup() as tg:
            tasks = {}
            for url in urls:
                tasks[url] = tg.create_task(fetch_url(session, url))

        for url, task in tasks.items():
            try:
                results.append(task.result())
            except:
                logger.warning(f"Skipping failed fetch: {url}")

    return results
