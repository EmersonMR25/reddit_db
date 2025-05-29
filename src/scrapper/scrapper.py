"""
Fetches Reddit posts and comments using PRAW, processes them into structured objects,
and prepares them for insertion into a Supabase database.

Author: AbdielDev  
Version: 1.0.0  
Last Updated: 2025-05-22
"""

from typing import List
from typing import Set
import os
from dotenv import load_dotenv
from datetime import datetime
import praw
from praw.models import MoreComments, Submission, Comment as PrawComment
# load the classes from table_model.py
from database.table_model import Post, Comment
# load the classes from db_manager.py
from database.db_manager import insert_posts, insert_comments, get_all_post_ids

# Load environment variables
load_dotenv()

# Initialize PRAW
reddit: praw.Reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME")
)

reddit.read_only = True

print("Reddit client initialized successfully.")

def scrape_subreddit(subreddit_name: str, post_limit: int = 5) -> tuple[list[Post], list[Comment]]:
    subreddit = reddit.subreddit(subreddit_name)
    # Use list to store posts and comments to store a batch and then inset them all at once
    # Do this to avoid hitting the rate limit of the Reddit/Praw/Supabase API
    posts: list[Post] = []
    comments: list[Comment] = []
    existing_ids: Set[str] = get_all_post_ids()
    for submission in subreddit.hot(limit=post_limit):
        try:
            if submission.id not in existing_ids:
                post = Post.from_reddit_post(submission)
                posts.append(post)
                # Load and extract comments
                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list():
                    if isinstance(comment, PrawComment):
                        db_comment = Comment.from_reddit_comment(comment)
                        comments.append(db_comment)

        except Exception as e:
            print(f"Failed to process submission {submission.id}: {e}")
            continue

    return posts, comments