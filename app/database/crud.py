from sqlalchemy.orm import Session


class CRUD:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model
    
    async def get(self, id):
        return self.db.query(self.model).get(id)
    
    async def get_all(self, *args, limit: int = None, offset: int = None):
        return self.db.query(self.model).filter(*args).limit(limit).offset(offset)
    
    async def create(self, obj_in):
        obj = self.model(**obj_in)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    async def update(self, obj, obj_in):
        for attr, value in obj_in.items():
            setattr(obj, attr, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    async def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()
        return obj
    

class CRUDUser(CRUD):
    
    async def get_by_email(self, email: str):
        return self.db.query(self.model).filter(self.model.email.__eq__(email)).first()


class CRUDInvalidToken(CRUD):

    async def get_by_token(self, token: str):
        return self.db.query(self.model).filter(self.model.token.__eq__(token)).first()