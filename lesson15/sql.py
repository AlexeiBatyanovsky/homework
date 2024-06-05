from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Tarif, Service, db_add_new_data


sqlite_database = "sqlite:///database.db"
engine = create_engine(sqlite_database, echo=False)

with Session(autoflush=False, bind=engine) as db:
    db_add_new_data(engine, db)

    qs = db.query(Tarif).all()
    print(1, qs)
    
    for q in qs:
        print(2, q)
    
    for service in qs[1].service:
        print(3, service)
    qs = db.query(Service).all()
    print(qs)
    