# app/deps.py
from app.database import SessionLocal

# Dependency: untuk mendapatkan koneksi DB di endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
