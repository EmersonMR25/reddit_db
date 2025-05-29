"""
Defines data models for Reddit posts and comments used for scraping and storing
information into the database. Includes utility methods for transforming PRAW
objects into serializable dataclass instances.

Author: AbdielDev  
Version: 1.0.0  
Last Updated: 2025-05-22
"""

# Libraries
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import praw
from praw.models import Submission, Comment as PrawComment

@dataclass
class Post:
    """
    Represents a Reddit post with relevant metadata for storage and processing.

    Attributes:
        subreddit (str): The subreddit where the post was made.
        post_id (str): Unique identifier of the post.
        title (str): Title of the post.
        date_created (datetime): Timestamp when the post was created.
        score (int): Upvote score of the post.
        post_description (str): Content of the post (selftext).
        post_url (str): URL to the post.
    """

    subreddit: str
    post_id: str
    title: str
    date_created: datetime
    score: int
    post_description: str
    post_url: str

    @staticmethod
    def from_reddit_post(submission: Submission) -> "Post":
        """
        Creates a Post instance from a PRAW Submission object.

        Args:
            submission (Submission): A Reddit post object from the PRAW API.

        Returns:
            Post: A Post instance with data extracted from the submission.
        """
        return Post(
            subreddit=submission.subreddit.display_name,
            post_id=submission.id,
            title=submission.title,
            date_created=datetime.fromtimestamp(submission.created_utc),
            score=submission.score,
            post_description=submission.selftext,
            post_url=submission.url
        )
    
    def to_dict(post: "Post") -> dict[str, Any]:
        """
        Converts a Post instance to a dictionary format for storage.

        Args:
            post (Post): The Post instance to convert.

        Returns:
            dict[str, Any]: A dictionary representation of the post.
        """
        return {
            "subreddit": post.subreddit,
            "post_id": post.post_id,
            "title": post.title,
            "date_created": post.date_created.isoformat(),
            "score": post.score,
            "post_description": post.post_description,
            "post_url": post.post_url
        }


@dataclass
class Comment:
    """
    Represents a Reddit comment associated with a specific post.

    Attributes:
        comment_id (str): Unique identifier of the comment.
        subreddit (str): Subreddit where the comment was posted.
        post_id (str): ID of the post the comment belongs to.
        comment_text (str): Content of the comment.
        date_created (datetime): Timestamp of comment creation.
        score (int): Upvote score of the comment.
    """

    comment_id: str
    subreddit: str
    post_id: str
    comment_text: str
    date_created: datetime
    score: int

    @staticmethod
    def from_reddit_comment(comment: PrawComment) -> "Comment":
        """
        Creates a Comment instance from a PRAW Comment object.

        Args:
            comment (Comment): A Reddit comment object from the PRAW API.

        Returns:
            Comment: A Comment instance with extracted data.
        """
        return Comment(
            comment_id=comment.id,
            subreddit=comment.subreddit.display_name,
            post_id=comment.link_id.split('_')[1],  # Extracts post ID from 't3_xyz'
            comment_text=comment.body,
            date_created=datetime.fromtimestamp(comment.created_utc),
            score=comment.score
        )
    
    def to_dict(comment: "Comment") -> dict[str, Any]:
        """
        Converts a Comment instance to a dictionary format for storage.

        Args:
            comment (Comment): The Comment instance to convert.

        Returns:
            dict[str, Any]: A dictionary representation of the comment.
        """
        return {
            "comment_id": comment.comment_id,
            "subreddit": comment.subreddit,
            "post_id": comment.post_id,
            "comment_text": comment.comment_text,
            "date_created": comment.date_created.isoformat(),
            "score": comment.score
        }
