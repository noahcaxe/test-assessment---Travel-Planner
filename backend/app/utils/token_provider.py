import datetime
from jose import jwt, JWTError
from app.core.config import settings

class TokenProvider:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM
        self.access_exp = settings.ACCESS_TOKEN_MINUTES
        self.refresh_exp = settings.REFRESH_TOKEN_DAYS

    def create_access_token(self, *, user_id: str) -> str:
        now = datetime.datetime.utcnow()
        payload = {
            "sub": str(user_id),
            "type": "access",
            "iat": now.timestamp(),
            "exp": (now + datetime.timedelta(minutes=self.access_exp)).timestamp()
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def create_refresh_token(self, *, user_id: str) -> str:
        now = datetime.datetime.utcnow()
        payload = {
            "sub": str(user_id),
            "type": "refresh",
            "iat": now.timestamp(),
            "exp": (now + datetime.timedelta(days=self.refresh_exp)).timestamp()
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def decode_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except JWTError as e:
            raise ValueError("Invalid token") from e
