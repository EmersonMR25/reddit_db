import os
import time
from typing import List
from supabase import create_client, Client
from dotenv import load_dotenv

from typing import Any

# load the classes from models.py
from database.table_model import Post, Comment

# LOAD THIS STUPID THING
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

print("Supabase URL:", url)
print("Supabase Key (partial):", key[:4] + "..." if key else "Key not found")


supabase: Client = create_client(url, key)

# Since I only  want to create a large database, I don't need to worry about updating or
# deleting entries. I will just insert new ones, and retrieve the whole database.

def get_supabase_client() -> Client:
    """
    Returns the Supabase client instance.
    
    This function initializes and returns a Supabase client using the URL and key
    loaded from environment variables.
    
    Returns:
        Client: The Supabase client instance.
    """
    return supabase

MAX_RETRIES: int = 3
RETRY_WAIT_SECONDS: int = 2

def insert_posts(posts: List[Post]) -> None:
    """
    Inserts a list of Post objects into the Supabase 'posts' table in batch.
    Retries on connection errors.
    """
    if not posts:
        return

    data: List[dict[str, Any]] = [post.to_dict() for post in posts]

    for attempt in range(MAX_RETRIES):
        try:
            supabase.table("posts").insert(data).execute()
            return  # success, exit function
        except Exception as e:
            print(f"[Attempt {attempt + 1}] Failed to insert posts: {e}")
            if "ConnectionTerminated" in str(e) and attempt < MAX_RETRIES - 1:
                print(f"Retrying in {RETRY_WAIT_SECONDS} seconds...")
                time.sleep(RETRY_WAIT_SECONDS)
            else:
                raise


def insert_comments(comments: List[Comment]) -> None:
    """
    Inserts a list of Comment objects into the Supabase 'comments' table in batch.
    Retries on connection errors.
    """
    if not comments:
        return

    data: List[dict[str, Any]] = [comment.to_dict() for comment in comments]

    for attempt in range(MAX_RETRIES):
        try:
            supabase.table("comments").insert(data).execute()
            return  # success
        except Exception as e:
            print(f"[Attempt {attempt + 1}] Failed to insert comments: {e}")
            if "ConnectionTerminated" in str(e) and attempt < MAX_RETRIES - 1:
                print(f"Retrying in {RETRY_WAIT_SECONDS} seconds...")
                time.sleep(RETRY_WAIT_SECONDS)
            else:
                raise