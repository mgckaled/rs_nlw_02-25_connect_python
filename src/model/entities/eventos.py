from sqlalchemy import Column, Integer, String

from src.model.configs.base import Base


class Eventos(Base):
    __tablename__ = "Eventos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
