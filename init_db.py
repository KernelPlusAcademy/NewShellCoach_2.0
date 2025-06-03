from app import db
from app import User  # Make sure User model is imported if defined in app.py

db.create_all()
print("✅ Database and tables created.")
