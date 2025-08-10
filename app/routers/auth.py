from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register():
    return {"message": "Register endpoint"}

@router.post("/login")
def login():
    return {"message": "Login endpoint"}
