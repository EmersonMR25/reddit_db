"""
Defines the FastAPI application, route setup, and HTML rendering.

Author: AbdielDev  
Version: 1.0.0  
Last Updated: 2025-05-22
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database.db_manager import count_posts_and_comments

app: FastAPI = FastAPI()

# Static files mounting
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/count")
async def count_entries():
    count_data = count_posts_and_comments()
    return count_data