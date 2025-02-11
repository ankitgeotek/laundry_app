# In your Python shell
from app.database import SessionLocal
from app.models import User  # Adjust the import based on your project structure

# Create a new session
db = SessionLocal()

# Now you can perform CRUD operations:
new_user = User(name="Alice", email="alice@example.com", password_hash="hashed_password")
db.add(new_user)
db.commit()
db.refresh(new_user)
print("New user ID:", new_user.id)

# Don’t forget to close the session when done
db.close()
