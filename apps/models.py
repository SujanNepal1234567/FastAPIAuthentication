from db.session import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text


class User(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)
    about = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    @classmethod
    def get_user(cls, email, db):
        user = db.query(cls).filter(email == email).first()
        return user
