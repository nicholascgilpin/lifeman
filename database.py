import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    income = Column(Integer)
    physiological_need = Column(String)
    safety_need = Column(String)
    love_and_belonging_need = Column(String)
    esteem_need = Column(String)
    self_actualization_need = Column(String)

def create_user(db_file: str, age: int, income: int, physiological_need: str, safety_need: str, love_and_belonging_need: str, esteem_need: str, self_actualization_need: str):
    engine = create_engine(f'sqlite:///{db_file}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = User(age=age,
                    income=income,
                    physiological_need=physiological_need,
                    safety_need=safety_need,
                    love_and_belonging_need=love_and_belonging_need,
                    esteem_need=esteem_need,
                    self_actualization_need=self_actualization_need)

    session.add(new_user)
    session.commit()
    
    return new_user.id

def update_user(db_file="user.db", user_id="username", age=None, income=None, physiological_need=None, safety_need=None, love_and_belonging_need=None, esteem_need=None, self_actualization_need=None):
    engine = create_engine(f'sqlite:///{db_file}')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    user = session.query(User).filter_by(id=user_id).first()
    if user is None:
        return "FAILURE"

    
    if age is not None:
        user.age = age
    if income is not None:
        user.income = income
    if physiological_need is not None:
        user.physiological_need = physiological_need
    if safety_need is not None:
        user.safety_need = safety_need
    if love_and_belonging_need is not None:
        user.love_and_belonging_need = love_and_belonging_need
    if esteem_need is not None:
        user.esteem_need = esteem_need
    if self_actualization_need is not None:
        user.self_actualization_need = self_actualization_need
    
    session.commit()

    return "SUCCESS"
    

def get_user(db_file: str, user_id: int):
    engine = create_engine(f'sqlite:///{db_file}')
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(id=user_id).first()

    # Convert user object to dictionary
    user_dict = {column.name: getattr(user, column.name) for column in user.__table__.columns}

    return user_dict