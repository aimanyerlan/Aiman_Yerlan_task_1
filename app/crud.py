from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def create_note(note: schemas.NoteCreate, db: AsyncSession):
    new_note = models.Note(text=note.text)
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note

async def get_all_notes(db: AsyncSession):
    result = await db.execute(select(models.Note))
    return result.scalars().all()
