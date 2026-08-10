from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.security import hash_password, verify_password


class AuthService:

    def __init__(self, db: Session):
        self.db = db

    def register(
        self,
        username: str,
        email: str,
        password: str,
    ):
        existing_user = (
            self.db.query(User)
            .filter(
                (User.username == username)
                | (User.email == email)
            )
            .first()
        )

        if existing_user:
            return None

        user = User(
            username=username,
            email=email,
            hashed_password=hash_password(password),
            role="user",
            is_active=True,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def authenticate_user(
        self,
        username: str,
        password: str,
    ):
        user = (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.hashed_password,
        ):
            return None

        return user