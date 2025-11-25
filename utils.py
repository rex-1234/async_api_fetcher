from rich.console import Console
from rich.logging import RichHandler
import logging
import json

# Rich logging
console = Console()
logger = logging.getLogger("async-fetcher")
logger.setLevel(logging.INFO)

handler = RichHandler(console=console, rich_tracebacks=True)
logger.addHandler(handler)
logger.propagate = False

def save_to_json(filename, data):
    """Save data to a JSON file."""
    with open (filename, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Data saved to {filename}")
