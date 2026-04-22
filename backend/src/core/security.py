import asyncio
import uuid
from datetime import UTC, datetime, timedelta

import bcrypt
import jwt

from src.core.config import JWTConfig
from src.core.dto import TokenClaims


def _hash_password_sync(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def _verify_password_sync(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


async def hash_password(password: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _hash_password_sync, password)


async def verify_password(password: str, hashed: str) -> bool:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _verify_password_sync, password, hashed)


def create_access_token(user_id: str, email: str, username: str, config: JWTConfig) -> str:
    now = datetime.now(UTC)
    payload = {
        "sub": user_id,
        "email": email,
        "username": username,
        "iat": now,
        "exp": now + timedelta(minutes=config.access_token_expire_minutes),
        "type": "access",
    }
    return jwt.encode(payload, config.secret, algorithm=config.algorithm)


def create_refresh_token() -> str:
    return uuid.uuid4().hex


def decode_access_token(token: str, config: JWTConfig) -> TokenClaims:
    payload = jwt.decode(token, config.secret, algorithms=[config.algorithm])
    return TokenClaims(sub=payload["sub"], email=payload["email"], username=payload["username"])
