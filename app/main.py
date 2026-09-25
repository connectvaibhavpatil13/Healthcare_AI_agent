from fastapi import FastAPI
from sqlalchemy import text
from app.api.routes.analytics import router as analytics_router
from app.database.connection import engine

app = FastAPI(
    title="Healthcare AI Analytics Agent",
    version="1.0.0"
)

app.include_router(analytics_router)

@app.get("/")
def root():
    return {
        "message": "Healthcare AI Analytics Agent is running"
    }


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }
