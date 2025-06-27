📐 BingePal – Architecture Overview

BingePal is a cross-platform demonstration project designed to showcase integration across:

    A FastAPI backend

    A Java-based Android mobile app

    A Web Dashboard with HTML/JS/Bootstrap

    A lightweight Admin Console using browser-based auth and log introspection

🧱 Project Structure
```
bingepal/
├── backend-python-api/
│   ├── app/
│   │   ├── api/           # All FastAPI route modules (e.g. search, history, devlogs)
│   │   ├── services/      # External API wrappers (TMDB, Anilist, etc.)
│   │   ├── utils/         # Utility code including memory logging
│   │   └── main.py        # FastAPI app entrypoint
├── bingepal-web/
│   ├── admin.html         # Auth-protected admin view for logs
│   ├── js/
│   │   └── admin.js       # SHA256 auth + fetch logs
├── bingepal-android/      # Android Studio Java app
└── logs/ (not used anymore)
```
⚙️ Backend (FastAPI)

    Python 3.11, served with uvicorn

    Modular routes under app/api, with clear separation of logic and endpoints

    Service abstractions under app/services, each calling external APIs

    Security: A simple SHA256-based token gate in devlogs.py, used in portfolio context

    Logging: Logs are captured in memory using a deque buffer instead of writing to dev.log

        Exposed with get_recent_logs() from utils/logger.py

Key Feature

    Logs stored in memory using deque for Render.com compatibility

    Accessed via /api/dev-logs route (token required)

🌐 Web Dashboard

    Static HTML served via GitHub Pages or local preview

    Bootstrap 5 UI

    Components:

        app.html, history.html, trends.html for browsing

        admin.html: Authenticated view of backend logs

    JS handles secure token hashing using browser-native crypto.subtle.digest

📱 Android App

    Written in Java

    Communicates with FastAPI backend via HTTP

    Built to simulate common media search and favorites flow

🔒 Admin Access

    A protected /api/dev-logs endpoint

    Token-based validation:

        SHA256 of the answer is checked against an env var STORED_HASH

        Token stored in browser memory after valid login

    Web frontend (admin.html) handles the auth prompt and log rendering

📤 Deployment

    Backend hosted on Render.com

        Logs stored in memory (stdout visible via Render's dashboard)

    Frontend static site hosted on GitHub Pages

    CI/CD: GitHub Actions for build and deploy:

        Sync from monorepo to subrepos

        Run backend test suite

        Deploy web assets to gh-pages

Simple code for demo readability

In-memory optimizations to adapt for free-tier hosting
