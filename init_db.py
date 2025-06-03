from app import app, db, User

# Ensure you're within the app context
with app.app_context():
    db.create_all()
    print("✅ Database and tables created successfully.")
