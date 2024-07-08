from fastapi import APIRouter
from zipsaservice.application.usecase.login import LoginUseCase, LoginInputDto

router = APIRouter()


@router.post("/login/access-token")
async def login_access_token(input: LoginInputDto):
    # token = await LoginUseCase().execute(input)
    pass




