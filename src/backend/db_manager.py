import os
from supabase import create_client, Client
from dotenv import load_dotenv

from typing import Any

# load the classes from models.py
from backend.table_model import Post, Comment

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

def insert_post(post: Post) -> None:
    """
    Inserts data into the POST table.
    """
    try:
        data: dict[str, Any] = post.to_dict()
        supabase.table("posts").insert(data).execute()
    except Exception as e:
        print(f"Failed to insert post: {e}")

def insert_comment(comment: Comment) -> None:
    """
    Inserts data into the COMMENT table.
    """
    try:
        data: dict[str, Any] = comment.to_dict()
        supabase.table("comments").insert(data).execute()
    except Exception as e:
        print(f"Failed to insert post: {e}")