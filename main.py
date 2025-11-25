import asyncio
from fetcher import fetch_all
from utils import save_to_json, logger

URLS = [
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
    "https://jsonplaceholder.typicode.com/users/3",
    "https://catfact.ninja/fact",
    "https://dog.ceo/api/breeds/image/random",
    "https://httpbin.org/get",
    "https://httpbin.org/uuid",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/comments/1",
    "https://jsonplaceholder.typicode.com/comments/2",
    "https://jsonplaceholder.typicode.com/comments/3"
]

async def main():
    logger.info("Starting URL fetcher")

    results = await fetch_all(URLS)

    logger.info(f"Fetched {len(results)} URLs successfully")
    save_to_json("fetched_data.json", results)

    logger.info("All Done!!!")

if __name__ == "__main__":
    asyncio.run(main())
