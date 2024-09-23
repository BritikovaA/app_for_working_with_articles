from sqlalchemy import select
from database import async_session, Articles
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete
from sqlalchemy.exc import SQLAlchemyError
from models import SArticleAdd


class ArticleDao:
    model = Articles

    @classmethod
    async def get_articles(cls):
        async with async_session() as session:
            query = select(Articles)
            result = await session.execute(query)
            articles_model = result.scalars().all()
        return articles_model

    @classmethod
    async def get_article_by_id(cls, article_id: int):
        async with async_session() as session:
            query = select(Articles).filter_by(id=article_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add_article(cls, article: SArticleAdd) -> int:
        async with async_session() as session:
            data = article.model_dump()
            new_article = Articles(**data)
            session.add(new_article)
            try:
                await session.flush()
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return new_article.id

    @classmethod
    async def update_article(cls, id, **values):
        async with async_session() as session:
            async with session.begin():
                query = (
                    sqlalchemy_update(cls.model)
                    .where(cls.model.id == id)
                    .values(**values)
                )
                result = await session.execute(query)
                try:
                    await session.flush()
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount

    @classmethod
    async def delete_article(cls, article_id: int = 0):
        async with async_session() as session:
            async with session.begin():
                query = sqlalchemy_delete(cls.model).filter_by(id=article_id)
                result = await session.execute(query)
                try:
                    await session.flush()
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount
