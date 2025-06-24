# BingePal

BingePal is an open-source platform for exploring Movies, Series, Anime, Books, Manga, and Games.

It includes:

- 📱 Android search app  
- 🚀 FastAPI backend for content search & tracking  
- 📊 Web dashboard using HTML, Bootstrap & Chart.js  

All parts connect via a shared REST API — no accounts, no ads, just a full-stack demo.

🔗 **Live Backend API**: [https://bingepal.onrender.com](https://bingepal.onrender.com)  
📄 **Docs**: [https://bingepal.onrender.com/docs](https://bingepal.onrender.com/docs)

## 🐳 Docker Support

To build and run the backend with Docker:

```bash
docker build -t bingepal-backend .
docker run --env-file .env -p 8000:8000 bingepal-backend
```

## ⚙️ CI/CD Workflows

Includes GitHub Actions for:

- ✅ Android build + lint  
- ✅ Backend testing  
- ✅ Web dashboard deployment  
- ✅ Auto-syncing subfolder repos

These workflows ensure continuous integration and consistent deployment across all components.
