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
    blocked = Column(String(25))   
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())   
    packages = relationship('Package', backref='user')
    
    def __init__(self, name:str, login:str, blocked = False) -> None:
        super().__init__()
        self.name = name
        self.login = login  
        self.blocked = blocked
    
    def __repr__(self):
        return f'{self.name}, {self.login}'
    
class Package(Base):  

    __tablename__ = 'package'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
                
    def __repr__(self):
        return f'{self.name}'

package_service = Table(
            'package_service',
            Base.metadata,
            Column('package_id', Integer, ForeignKey('package.id')),
            Column('service_id', Integer, ForeignKey('service.id')),
            )

class Service(Base):    
    __tablename__ = 'service'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(250), nullable=False)
    status = Column(String(100), nullable=False)
    price = Column(String(100), nullable=False)
    tarif = relationship('Package', 
                           secondary=package_service,
                           backref = 'service')
    
    def __init__(self, name:str, status, price) -> None:
        super().__init__()
        self.name = name
        self.status = status  
        self.price = price
       
    def __repr__(self):
        return f'{self.name}'
    
    
def db_add_new_data(engine, db):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    users = [
            User('Вася','user1', True), 
            User('Петя','user2', False),
            User('Антон','user3')
    ]
    
    
    package1 = Package(name='Package of services N1', user=users[0])
    package2 = Package(name='Package of services N2', user=users[1])
    
    service_list = [
        Service('Internet', 'standart', '5'),
        Service('Internet unlim+', 'premium', '15'),
        Service('TV 30', 'standart', '5'),
        Service('TV 200+', 'premium', '10'),
        Service('CCTV', 'premium+', '25'),              
    ]

    package1.service.append(service_list[0])
    package1.service.append(service_list[2])
    package1.service.append(service_list[3])
   

    package2.service.append(service_list[1])
    package2.service.append(service_list[2])
    package2.service.append(service_list[4])  
    
    db.add_all(users) 
    
    db.commit()


