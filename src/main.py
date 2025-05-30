"""
Main entry point for the Reddit scraper web application.

- Starts the FastAPI app to serve frontend content.
- Runs an initial data scrape.
- Starts the recurring scheduler job to scrape every 6 hours.

Author: AbdielDev  
Version: 1.0.0  
Last Updated: 2025-05-22
"""

from backend.web_app import app  # FastAPI app instance
from scrapper.scheduler import scheduler, scheduled_scrape
import threading

def start_scraper() -> None:
    print("🔄 Running initial scrape...")
    scheduled_scrape()

    print("⏱️ Starting scheduler...")
    scheduler.start()

# Run the scraper and scheduler in a separate thread
scraper_thread = threading.Thread(target=start_scraper, daemon=True)
scraper_thread.start()