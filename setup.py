"""
Scripts to run to set up our database
"""

from model import db, User, Task
from passlib.hash import pbkdf2_sha256


# Create the database tables for our model
db.connect()
db.drop_tables([User, Task], True)
db.create_tables([User, Task])

# We need a user to log in as! Create it here.
first_user_name = "admin"
first_user_password = "password"

first_user = User(name=first_user_name, password=pbkdf2_sha256.hash(first_user_password))
first_user.save()
