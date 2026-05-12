from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.model.travelproject import TravelProject


class ProjectRepository:

    async def create(
        self,
        session: AsyncSession,
        user_id: int,
        name: str,
        description: str | None,
        start_date,
    ) -> TravelProject:

        project = TravelProject(
            user_id=user_id,
            name=name,
            description=description,
            start_date=start_date,
        )

        session.add(project)

        await session.commit()
        await session.refresh(project)

        return project

    async def get_by_id(
        self,
        session: AsyncSession,
        project_id: int,
    ) -> TravelProject | None:

        stmt = (
            select(TravelProject)
            .where(TravelProject.id == project_id)
            .options(
                selectinload(
                    TravelProject.places
                )
            )
        )

        result = await session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all_by_user(
        self,
        session: AsyncSession,
        user_id: int,
    ) -> list[TravelProject]:

        stmt = (
            select(TravelProject)
            .where(
                TravelProject.user_id == user_id
            )
            .order_by(
                TravelProject.id.desc()
            )
        )

        result = await session.execute(stmt)

        return list(result.scalars().all())

    async def update(
        self,
        session: AsyncSession,
        project: TravelProject,
    ) -> TravelProject:

        session.add(project)

        await session.commit()
        await session.refresh(project)

        return project

    async def delete(
        self,
        session: AsyncSession,
        project: TravelProject,
    ) -> None:

        await session.delete(project)

        await session.commit()


project_trav_repo = ProjectRepository()