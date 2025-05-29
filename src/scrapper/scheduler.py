from apscheduler.schedulers.blocking import BlockingScheduler
from scrapper.scrapper import scrape_subreddit
from database.db_manager import insert_posts, insert_comments

scheduler: BlockingScheduler = BlockingScheduler()

@scheduler.scheduled_job("interval", hours=6)
def scheduled_scrape() -> None:
    """
    Scheduled job to scrape subreddits and insert into Supabase.
    """
    print("Scraping subreddits...")
    subreddits: list[str] = ["wallstreetbets", "stocks"]
    
    for subreddit in subreddits:
        print(f"Scraping: {subreddit}")
        posts, comments = scrape_subreddit(subreddit, post_limit=50)

        print(f"Inserting {len(posts)} posts and {len(comments)} comments for {subreddit}...")
        insert_posts(posts)
        insert_comments(comments)

    print("Scraping cycle completed.")

if __name__ == "__main__":
    print("Running initial scrape...")
    scheduled_scrape()  # Run once immediately
    print("Scheduler started...")
    scheduler.start()
