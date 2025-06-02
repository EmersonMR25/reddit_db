# 🧠 Reddit Scraper & Dashboard

A simple full-stack web application that scrapes data from a specified subreddit using PRAW (Python Reddit API Wrapper), stores it in a Supabase database, and displays it via a FastAPI-powered frontend with HTMl for lightweight interaction.

- Link: https://reddit-db-tj8k.onrender.com/ (Give it 3 mins to start because I'm using Render)
- Built with ❤️ by [@EmersonMR25](https://github.com/EmersonMR25)
- ChatGPT was used to develop the html & CSS, as well as all the documentation code.

---

## 🚀 Features

- Scrapes Reddit posts and comments from any public subreddit.
- Automatically stores data in a Supabase PostgreSQL database.
- Displays the data in a clean, minimal HTML frontend.
- Supports scheduled scraping every 6 hours using `APScheduler`.

---

## 🧰 Technologies Used

- **Python 3.11+**
- **FastAPI** – for the backend API and server
- **PRAW** – to interface with Reddit
- **Supabase** – as the backend database (PostgreSQL)
- **HTML** – for minimal frontend interactions
- **Uvicorn** – ASGI server to run the app
- **APScheduler** – for background job scheduling
- **dotenv** – for handling environment variables

---

## 📦 Requirements

Install the following Python packages:

```bash
pip install -r requirements.txt
```

---
⚙️ Environment Variables
Create a .env file in the root of your project with the following:

```bash
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=
REDDIT_USERNAME=
REDDIT_PASSWORD=
REDDIT_SUBREDDIT=

SUPABASE_URL=
SUPABASE_KEY=
```
---
# 🛠 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/EmersonMR25/reddit_db.git
```
```bash
cd reddit_db
```

### 2. (Optional but recommended) Create a virtual environment
```bash
python -m venv venv
```
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create the .env file with your Reddit and Supabase credentials
```bash
touch .env
```
Then paste your values into .env

### 5. enter the src folder
```bash
cd src/
```
```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

Visit http://localhost:8000 to view the app.

---
### Triggering the Scraper Manually
To start the scraper and scheduler manually:

```bash
python -m scrapper.scheduler
```
- It will:
- Run an immediate scrape on startup
- Continue scraping every 6 hours in the background

---

📝 License
MIT License.
Feel free to fork and customize for your own projects!

💬 Feedback
If you find bugs or have suggestions, open an issue or submit a PR on GitHub.

Let me know if you'd like me to generate this as a file or help tailor the deployment section for a different platform like Vercel or Fly.io!