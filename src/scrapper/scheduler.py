from apscheduler.schedulers.blocking import BlockingScheduler
from scrapper.scrapper import scrape_subreddit

scheduler: BlockingScheduler = BlockingScheduler()

@scheduler.scheduled_job("interval", hours=6)
def scheduled_scrape() -> None:
    """
    Scheduled job to scrape subreddits
    """
    print("Scraping subreddits...")
    subreddits: list[str] = ["wallstreetbets", "stocks", "StockMarket"]
    for subreddit in subreddits:
        scrape_subreddit(subreddit, post_limit=100)


if __name__ == "__main__":
    # Start the scheduler
    print("Scheduler started...")
    scheduler.start()