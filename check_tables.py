# check_tables.py
from sqlalchemy import create_engine, inspect

# Ganti sesuai DATABASE_URL yang kamu pakai di .env
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/tasknest"

# Buat koneksi ke database
engine = create_engine(DATABASE_URL)

# Gunakan inspector untuk lihat tabel
inspector = inspect(engine)
tables = inspector.get_table_names()

print("📋 Daftar tabel di database:")
if tables:
    for tbl in tables:
        print(f"- {tbl}")
else:
    print("⚠️ Tidak ada tabel ditemukan.")

# Tutup koneksi
engine.dispose()
