from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Package, Service, db_add_new_data


sqlite_database = "sqlite:///database.db"
engine = create_engine(sqlite_database, echo=False)

with Session(autoflush=False, bind=engine) as db:
    db_add_new_data(engine, db)

    db_query = db.query(Package).all()
    print(db_query)
   
    db_query2 = db.query(Service).all()
    print(db_query2)
    