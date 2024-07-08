from fastapi import APIRouter
from zipsaservice.application.usecase.login import LoginUseCase, LoginInputDto

router = APIRouter()


@router.get("/accounts/{account_id}")
async def login_access_token(account_id: str):
    # token = await LoginUseCase().execute(input)
    pass
