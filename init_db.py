from app import db, User
from app import app  # Make sure the app context is available

# Create the database and tables
with app.app_context():
    db.create_all()
    print("✅ Database and tables created successfully.")
