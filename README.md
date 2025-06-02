# 🧠 Reddit Scraper & Dashboard

A simple full-stack web application that scrapes data from a specified subreddit using PRAW (Python Reddit API Wrapper), stores it in a Supabase database, and displays it via a FastAPI-powered frontend with HTMl for lightweight interaction.

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
Make sure your requirements.txt includes:

txt
Copy
Edit
fastapi==0.110.1
praw==7.7.1
supabase==1.2.0
uvicorn==0.29.0
python-dotenv==1.0.1
httpx==0.27.0
⚙️ Environment Variables
Create a .env file in the root of your project with the following:

env
Copy
Edit
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=
REDDIT_USERNAME=
REDDIT_PASSWORD=
REDDIT_SUBREDDIT=

SUPABASE_URL=
SUPABASE_KEY=

🛠 Installation & Setup
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/EmersonMR25/reddit_db.git
cd reddit_db

# 2. (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create the .env file with your Reddit and Supabase credentials
touch .env
# Then paste your values into .env
Running the App
Locally
To run the FastAPI app:

# 5. enter the src folder
bash
Copy
Edit
cd src/

bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 10000
Visit http://localhost:8000 to view the app.

Triggering the Scraper Manually
To start the scraper and scheduler manually:

bash
Copy
Edit
python -m scrapper.scheduler
It will:

Run an immediate scrape on startup

Continue scraping every 6 hours in the background

Deployment (Render)
If deploying to Render:

Upload your .env variables through Render's dashboard.

Use the following Start Command:

bash
Copy
Edit
uvicorn src.main:app --host 0.0.0.0 --port 10000
Ensure the root directory is the repository root (not /src).

📝 License
MIT License.
Feel free to fork and customize for your own projects!

💬 Feedback
If you find bugs or have suggestions, open an issue or submit a PR on GitHub.

vbnet
Copy
Edit

Let me know if you'd like me to generate this as a file or help tailor the deployment section for a different platform like Vercel or Fly.io!