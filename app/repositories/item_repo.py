from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.models.item import Item
from app.schemas.item_services import ItemCreate


class ItemRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_all(self) -> list[Item]:
        result = await self.session.execute(select(Item))
        return result.scalars().all()
    
    async def get_by_id(self, guid: UUID) -> Item | None:
        result = await self.session.execute(select(Item).where(Item.guid == guid))
        return result.scalar_one_or_none()
    
    async def create(self, data: ItemCreate) -> Item:
        item = Item(**data.model_dump())
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item