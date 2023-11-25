from app import app,db
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey,Enum

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        pass

