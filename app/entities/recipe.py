from sqlalchemy import Column, Integer, String, DateTime, func ,Text
from app.db.session import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    recipe_name = Column(String)
    ingredients = Column(Text)
    methode = Column(Text)
    region = Column(String)

    def save(self, db):
        db.add(self)
        db.commit()

    @staticmethod
    def getAll(db):
        apps = db.query(Recipe).all()
        return apps
    
    @staticmethod
    def deleteOne(id, db):
        db.query(Recipe).filter(Recipe.id == id).delete()
        db.commit()
        
    @staticmethod
    def deleteAll(db):
        db.query(Recipe).delete()
        db.commit()

    def __str__(self):
       return f"app(id={self.id}, name={self.name}, email={self.kubeconfig_file_id})"