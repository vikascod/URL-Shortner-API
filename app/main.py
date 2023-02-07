from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app import models
import random

models.Base.metadata.create_all(engine)

app = FastAPI()

@app.post("/shorten")
async def shorten_url(url: str, db:Session=Depends(get_db)):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    tiny_url_id = ''.join(random.choices(char, k=6))
    tiny_url = f"http://localhost:8000/{tiny_url_id}"
    tiny = models.TinyURL(original_url=url, tiny_url=tiny_url)
    db.add(tiny)
    db.commit()
    return {"tiny_url": tiny_url}


@app.get("/{tiny_url_id}")
async def redirect_url(tiny_url_id: str, db:Session=Depends(get_db)):
    tiny = db.query(models.TinyURL).filter_by(tiny_url=f"http://localhost:8000/{tiny_url_id}").first()
    if not tiny:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    return {'url':tiny.original_url}