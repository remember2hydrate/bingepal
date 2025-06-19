# BingePal

**BingePal** is an open-source platform for exploring Movies, Series, Anime, Books, Manga and Games.

It consists of:

- 📱 An Android search app
- 🚀 A FastAPI backend for search & data tracking
- 📊 A web dashboard built with HTML + Bootstrap + Chart.js

All parts communicate via a shared REST API - no accounts, no ads, just a full-stack demo project.

## ⚙️ CI/CD Workflows

This project includes GitHub Actions pipelines for:

- ✅ Linting and building the Android app  
- ✅ Running backend tests on every push  
- ✅ Deploying the web dashboard automatically  
- ✅ Scheduled auto-sync to mirror subfolder projects into their respective standalone repos 

These workflows ensure consistent integration and deployment across all components.
