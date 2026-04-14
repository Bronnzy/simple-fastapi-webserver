from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    discount: float | None = None
    tax: float | None = None
    


class ItemResponse(BaseModel):
    guid: UUID
    name: str
    description: str | None = None
    price: float
    discount: float | None = None
    tax: float | None = None
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "examples": [
                {
                    'guid': "550e8400-e29b-41d4-a716-446655440000",
                    'name': "Apple",
                    'description': "Lorem ipsum",
                    'price': 46.78,
                    'discount': 25,
                    'tax': 12.5,
                    'created_at': "2018-03-22T08:30:58.005",
                    'updated_at': "2018-03-22T08:35:58.005",
                }
            ]
        }
    )
    