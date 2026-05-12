import uuid
from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.token import RefreshToken


class TokenRepository:

    async def create(
        self,
        session: AsyncSession,
        user_id: uuid.UUID,
        token_hash: str,
        expires_at: datetime,
    ) -> RefreshToken:

        token = RefreshToken(
            id=uuid.uuid4(),
            user_id=user_id,
            token_hash=token_hash,
            expires_at=expires_at,
        )

        session.add(token)

        await session.flush()
        await session.refresh(token)

        return token

    async def get_by_hash(
        self,
        session: AsyncSession,
        token_hash: str,
    ) -> RefreshToken | None:

        stmt = select(RefreshToken).where(
            RefreshToken.token_hash == token_hash
        )

        result = await session.execute(stmt)

        return result.scalar_one_or_none()

    async def revoke(
        self,
        session: AsyncSession,
        token: RefreshToken,
    ) -> None:

        token.revoked = True

        session.add(token)

        await session.flush()

    async def revoke_all_by_user(
        self,
        session: AsyncSession,
        user_id: uuid.UUID,
    ) -> None:

        stmt = (
            update(RefreshToken)
            .where(
                RefreshToken.user_id == user_id,
                RefreshToken.revoked.is_(False),
            )
            .values(revoked=True)
        )

        await session.execute(stmt)


token_repo = TokenRepository()