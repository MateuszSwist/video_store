from sqlalchemy.orm import sessionmaker
from session import engine
from models import Base

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
