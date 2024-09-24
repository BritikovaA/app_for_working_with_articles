from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("sqlite+aiosqlite:///sql_21vek_app.db")


class Model(DeclarativeBase):
    pass


class Articles(Model):
    __tablename__ = "artiсles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str]
    author: Mapped[str | None]
    source: Mapped[str | None]


async_session = async_sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)
