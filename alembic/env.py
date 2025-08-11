from logging.config import fileConfig
import os
from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Ambil DATABASE_URL dari .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Import metadata dari models
from app.models import Base  # Pastikan Base sudah didefinisikan di models.py

# Config dari alembic.ini
config = context.config

# Kalau ingin logging sesuai alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata untuk autogenerate migration
target_metadata = Base.metadata

def run_migrations_offline():
    """Jalankan migrasi dalam mode offline."""
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Jalankan migrasi dalam mode online."""
    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
