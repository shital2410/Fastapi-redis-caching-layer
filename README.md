# Build a Caching Layer for an API

This project implements a high-performance caching layer using **FastAPI** and **Redis** to optimize API response times.

## 🚀 Setup & Installation
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn redis
   ```
2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## 📊 Performance Comparison (Results)
* **Without Cache (Cache Miss):** **2.0 seconds** (Fetched from simulated database).
* **With Cache (Cache Hit):** **< 5 milliseconds** (Fetched instantly from Redis RAM).

## 💡 Caching Strategies Implemented
1. **TTL (Time-To-Live):** Cache automatically expires and updates every 60 seconds.
2. **Cache Invalidation:** Using `POST /update-data` to clear stale data instantly when changes occur.
