import time
import json
from fastapi import FastAPI
import redis

app = FastAPI()

# Connect to the local Redis instance
# decode_responses=True ensures that we get clean string data instead of byte data
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def heavy_database_query():
    """Simulates a slow database query or time-consuming calculation."""
    time.sleep(2) # Simulates a 2-second delay
    return {"status": "success", "message": "This data is fetched from the primary database"}


@app.get("/get-api-data")
def get_api_data():
    cache_key = "my_api_cache_key"
    
    # 1. Check if the data exists in Redis cache
    cached_data = r.get(cache_key)
    
    if cached_data:
        # Cache Hit: Return the cached data instantly
        return {"source": "Cache (Fast)", "data": json.loads(cached_data)}
    
    # 2. Cache Miss: Fetch the fresh data from the slow database
    fresh_data = heavy_database_query()
    
    # 3. Store the fresh data into Redis cache with a 60-second expiration time (TTL)
    r.setex(cache_key, 60, json.dumps(fresh_data))
    
    return {"source": "Database (Slow)", "data": fresh_data}


@app.post("/update-data")
def update_data():
    """Handles Cache Invalidation when the underlying database changes."""
    cache_key = "my_api_cache_key"
    
    # Simulating a database update operation here...
    
    # 4. Invalidate (Delete) the old cache key to avoid serving stale data
    r.delete(cache_key)
    
    return {"status": "success", "message": "Database updated and cache invalidated successfully"}