from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.user import User


class UserRepository:

    async def create(
        self,
        session: AsyncSession,
        email: str,
        password_hash: str,
    ) -> User:

        user = User(
            email=email,
            password_hash=password_hash,
        )

        session.add(user)

        await session.commit()
        await session.refresh(user)

        return user

    async def get_by_id(
        self,
        session: AsyncSession,
        user_id: int,
    ) -> User | None:

        stmt = select(User).where(
            User.id == user_id
        )

        result = await session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_email(
        self,
        session: AsyncSession,
        email: str,
    ) -> User | None:

        stmt = select(User).where(
            User.email == email
        )

        result = await session.execute(stmt)

        return result.scalar_one_or_none()

    async def delete(
        self,
        session: AsyncSession,
        user: User,
    ) -> None:

        await session.delete(user)

        await session.commit()


user_repo = UserRepository()
