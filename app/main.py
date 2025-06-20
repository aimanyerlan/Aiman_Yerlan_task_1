from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from . import models, schemas, crud
from .database import engine, Base, get_session

app = FastAPI(title="Notes API")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/notes", response_model=schemas.NoteOut)
async def create_note(note: schemas.NoteCreate, db: AsyncSession = Depends(get_session)):
    return await crud.create_note(note, db)

@app.get("/notes", response_model=List[schemas.NoteOut])
async def read_notes(db: AsyncSession=Depends(get_session)):
    return await crud.get_all_notes(db)