from uuid import UUID
from datetime import datetime
from sqlalchemy import text, types, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Item(Base):
    __tablename__ = 'items'
    guid: Mapped[UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        init=False,
        server_default=text('gen_random_uuid()')
    )
    name: Mapped[str] = mapped_column(types.String)
    description: Mapped[str] = mapped_column(types.String)
    price: Mapped[float] = mapped_column(types.Float)
    discount: Mapped[float] = mapped_column(types.Float)
    tax: Mapped[float] = mapped_column(types.Float)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
