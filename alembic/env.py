import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from dotenv import load_dotenv

# Load environment variables dari .env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Masukkan folder utama project ke sys.path
sys.path.insert(0, BASE_DIR)

# Import Base dan model
from app.deps import Base, DATABASE_URL
import app.models  # Pastikan ini mengimport semua model

# Konfigurasi Alembic
config = context.config

# Gunakan file alembic.ini untuk logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata dari semua model ORM
target_metadata = Base.metadata

# Set URL database dari .env
config.set_main_option("sqlalchemy.url", DATABASE_URL)

def run_migrations_offline():
    """Jalankan migrasi dalam mode 'offline'."""
    ur
