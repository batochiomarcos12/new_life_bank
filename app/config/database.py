import os
from datetime import datetime
from sqlalchemy import column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import datetime
from sqlalchemy.ext.declarative import declared_attr,declarative_base

SQLALCHEMY_DATABASE_URL=os.getenv("DATABASE_URL","sqlite///mydatabase.db")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BaseModel(object):
    @declared_attr
    def created_at(cls):
        return column(Datetime,default=datetime.now)

Base= declarative_base(cls=BaseModel)

def get_db():
    db=None
    try:
        db = SessionLocal()
        Base.Metadate.create_all(engine)
        yield db
        finally:
            if db:
                db.close()