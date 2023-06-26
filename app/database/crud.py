from sqlalchemy.orm import Session


class CRUD:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model
    
    def get(self, id):
        return self.db.query(self.model).get(id)
    
    def get_all(self):
        return self.db.query(self.model).all()
    
    def create(self, obj_in):
        obj = self.model(**obj_in)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, obj, obj_in):
        for attr, value in obj_in.items():
            setattr(obj, attr, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()
        return obj
