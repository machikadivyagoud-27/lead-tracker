from fastapi import FastAPI
from app.api.v1.router import router
from app.models.user import User 


app = FastAPI(
    title="Property Lead Tracker API",
    version="1.0.0"
)


@app.get("/api/v1/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(router, prefix="/api/v1")