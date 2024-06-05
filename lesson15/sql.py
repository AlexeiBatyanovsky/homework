from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Package, Service, db_add_new_data


sqlite_database = "sqlite:///database.db"
engine = create_engine(sqlite_database, echo=False)

with Session(autoflush=False, bind=engine) as db:
    db_add_new_data(engine, db)

    db_query = db.query(Package).all()
    print(db_query)
    
    for n in db_query:
        print(2, n)
    
    for service in db_query[1].service:
        print(3, service)
    qs = db.query(Service).all()
    print(qs)
    