from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from models import SArticle, SArticleAdd
from article_dao import *
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("templates/index.html")


@app.get("/articles/")
async def get_articles():
    articles = await ArticleDao.get_articles()
    return articles


@app.get("/articles/{article_id}")
async def get_article_by_id(article_id: int) -> SArticle | None:
    art_id = await ArticleDao.get_article_by_id(article_id)
    return art_id


@app.post("/new_article")
async def add_article(art: SArticleAdd = Depends()) -> dict:
    new_art_id = await ArticleDao.add_article(art)
    if new_art_id:
        return {"message": "Article added", "id": new_art_id}
    else:
        return {"message": "Something goes wrong!"}


@app.put("/update_article/{article_id}")
async def update_article(article_id: int, art: SArticleAdd = Depends()) -> dict:
    update_art = await ArticleDao.update_article(article_id, title=art.title, text=art.text, author=art.author,
                                                 source=art.source)
    if update_art:
        return {"message": "Article updated"}
    else:
        return {"message": "Something goes wrong!"}


@app.delete("/delete_article/{article_id}")
async def update_article(article_id: int) -> dict:
    delete_art = await ArticleDao.delete_article(article_id)
    if delete_art:
        return {"message": "Article deleted"}
    else:
        return {"message": "Something goes wrong!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8060, reload=True)
