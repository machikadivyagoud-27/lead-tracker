from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.jwt import create_access_token
from app.database.database import get_db
from app.schemas.auth import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.dependencies.auth import get_current_user
from app.models.user import User


from app.schemas.auth import LoginRequest


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    new_user = service.register(
        username=user.username,
        email=user.email,
        password=user.password,
    )

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Username or email already exists",
        )

    return new_user

@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    user = service.authenticate_user(
        data.username,
        data.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "username": user.username,
            "role": user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
        "is_active": current_user.is_active,
    }