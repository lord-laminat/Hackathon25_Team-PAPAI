from sqlalchemy.orm import Session
from typing import Generic, TypeVar, Type, Optional, List, Union, Dict, Any
from pydantic import BaseModel

ModelType = TypeVar("ModelType")

# Базовый класс репозитория.


class BaseRepository(Generic[ModelType]):
    # Конструктор. Принимает сессию бд и модель с которой работаем
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    # -- БАЗОВЫЕ МЕТОДЫ ВСЕХ НАСЛЕДНИКОВ AHEAD --
    # 1. Получить объект по его ID
    def get(self, id: int) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    # 2. Создать объект
    def create(self, obj_in: BaseModel) -> ModelType:
        # Превращаем Pydantic-схему в словарь, а потом в ORM-объект
        db_obj = self.model(**obj_in.dict())
        self.db.add(db_obj)    # Добавляем в сессию
        self.db.commit()       # Сохраняем изменения в БД
        # Обновляем объект (чтобы получить его с ID сгенерированным БД)
        self.db.refresh(db_obj)
        return db_obj

    # 3. Удалить объект по ID
    def remove(self, id: int) -> ModelType:
        obj = self.db.query(self.model).get(id)  # Находим объект
        self.db.delete(obj)    # Удаляем его
        self.db.commit()       # Сохраняем изменения
        return obj

    # 4. Обновить информацию об объектах
    def update(self, db_obj: ModelType, obj_in: Union[BaseModel, Dict[str, Any]]) -> ModelType:
        # Преобразуем объект Pydantic в словарь, если это необходимо
        if isinstance(obj_in, BaseModel):
            # Исключаем не переданные поля
            update_data = obj_in.dict(exclude_unset=True)
        else:
            update_data = obj_in

        # Обновляем поля объекта
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])

        # Сохраняем изменения
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
