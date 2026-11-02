
from database.database import engine, Base
from models.models import Department, User, Employee

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
