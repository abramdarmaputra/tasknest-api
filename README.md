# TaskNestAPI

## 🌟 Deskripsi Proyek

**TaskNestAPI** adalah RESTful API berbasis **FastAPI** untuk manajemen tugas (to-do list).
API ini memungkinkan pengguna untuk membuat, membaca, memperbarui, dan menghapus tugas, serta mendukung autentikasi berbasis **JWT**.
Dapat digunakan sebagai backend aplikasi mobile maupun web.

---

## 🎯 Tujuan

* Menyediakan layanan backend yang cepat dan ringan untuk manajemen tugas.
* Mempermudah integrasi dengan aplikasi frontend/mobile.
* Menerapkan autentikasi dan otorisasi berbasis token.

---

## 🛠️ Teknologi yang Digunakan

* **Python** (FastAPI)
* **PostgreSQL** (Database)
* **SQLAlchemy** (ORM)
* **Alembic** (Migrasi Database)
* **Docker** & **docker-compose** (Containerization)
* **Postman** (Pengujian API)
* **GitHub** (Version Control)

---

## 🛠️ Panduan Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/abramdarmaputra/tasknest-api.git
cd tasknest-api
```

### 2. Buat Virtual Environment

```bash
python -m venv venv         # MacOS/Linux
source venv/bin/activate    # Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment

Buat file `.env` berdasarkan `.env.example`:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/tasknest_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Setup Database

```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

### 6. Jalankan Server

```bash
uvicorn app.main:app --reload
```

---

## 📂 Struktur Direktori

```
tasknest-api/
├── alembic/               # File migrasi database
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── app/
│   ├── routers/           # Endpoint API
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── tasks.py
│   ├── __init__.py
│   ├── database.py        # Koneksi database
│   ├── deps.py            # Dependency injection
│   ├── main.py            # Entry point FastAPI
│   ├── models.py          # ORM models
│   ├── schemas.py         # Pydantic schemas
├── tests/                 # Unit & integration tests
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_tasks.py
├── .env.example
├── alembic.ini
├── check_tables.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── venv/
```

---

## 📊 Endpoint Utama

### **Auth**

* `POST /auth/register` – Registrasi user baru
* `POST /auth/login` – Login dan mendapatkan JWT token
* `GET /auth/me` – Mendapatkan profil user yang sedang login

### **Tasks**

* `GET /tasks/` – List semua tugas
* `POST /tasks/` – Tambah tugas baru
* `PUT /tasks/{id}` – Update tugas
* `DELETE /tasks/{id}` – Hapus tugas

---

## 🧪 Testing API di Postman

1. Import file koleksi Postman (`TaskNestAPI.postman_collection.json`) jika tersedia.
2. Pastikan server berjalan di `http://localhost:8000`.
3. Uji semua endpoint CRUD dan autentikasi.

---

## 📝 Lisensi

```
Proyek ini menggunakan lisensi **MIT**.
```
