from fastapi import APIRouter

router = APIRouter()


@router.post("/login/access-token")
def login_access_token():
    pass