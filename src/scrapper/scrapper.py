from typing import List
import os
from dotenv import load_dotenv
from datetime import datetime

import praw
from praw.models import MoreComments, Submission, Comment as PrawComment

from database.table_model import Post, Comment
from database.db_manager import insert_posts, insert_comments

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

    posts: list[Post] = []
    comments: list[Comment] = []

    for submission in subreddit.hot(limit=post_limit):
        try:
            # Use the reusable constructor
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