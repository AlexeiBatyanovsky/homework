from sqlalchemy import (Column, ForeignKey, Table,
                        Integer, String, Text, Boolean, Date, DateTime)

from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    ...
    
    
class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25)) 
    login = Column(String(25))
    bloked = Column(String(25))   
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())   
    tarifs = relationship('Tarif', backref='user')
    
class Tarif(Base):  

    __tablename__ = 'tarif'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())   
            
    def __repr__(self):
        return f'{self.name}'

tarif_usluga = Table(
            'tarif_usluga',
            Base.metadata,
            Column('tarif_id', Integer, ForeignKey('tarif.id')),
            Column('usluga_id', Integer, ForeignKey('usluga.id')),
            )

class Usluga(Base):    
    __tablename__ = 'usluga'
    
    id = Column(Integer(), primary_key=True)
    question = Column(String(250), nullable=False)
    answer = Column(String(100), nullable=False)
    wrong1 = Column(String(100), nullable=False)
    tarif = relationship('Tarif', 
                           secondary=tarif_usluga,
                           backref = 'usluga')
    
    def __init__(self, question:str, answer, wrong1) -> None:
        super().__init__()
        self.question = question
        self.answer = answer  
        self.wrong1 = wrong1
       
    def __repr__(self):
        return f'{self.question}'
    
    
def db_add_new_data(engine, db):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    users = [
            User(name='Вася'), 
            User(name='User2'),
            User(name='User3')
    ]
    
    
    tarif1 = Tarif(name='Тариф N1', user=users[0])
    tarif2 = Tarif(name='Тариф N2', user=users[1])
    
    usluga_list = [
        Usluga('Internet', 'standart', '5'),
        Usluga('Internet unlim+', 'premium', '15'),
        Usluga('TV 30 ch', 'standart', '5'),
        Usluga('TV 200+ ch', 'premium', '10'),
        Usluga('CCTV', 'premium+', '25'),              
    ]

    tarif1.usluga.append(usluga_list[0])
    tarif1.usluga.append(usluga_list[2])
    tarif1.usluga.append(usluga_list[3])
   

    tarif2.usluga.append(usluga_list[1])
    tarif2.usluga.append(usluga_list[2])
    tarif2.usluga.append(usluga_list[4])  
    
    db.add_all(users) 
    
    db.commit()


