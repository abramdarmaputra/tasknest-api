from fastapi import FastAPI
from app.routers import auth, tasks

app = FastAPI(
    title="TaskNest API",
    description="API Service untuk Pengelolaan Tugas",
    version="0.1.0"
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Welcome to TaskNest API"}
