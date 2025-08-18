#📍 snippet ⇒ mod-user-model
# Modelo SQLModel para usuario con id, username y hashed_password
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str


