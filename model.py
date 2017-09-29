from peewee import Model, CharField, DateTimeField, ForeignKeyField
import os
#from playhouse.sqlite_ext import SqliteExtDatabase


#db = SqliteExtDatabase('my_database.db')

# heroku run -s free -- python setup.py
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class User(Model):
    name = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)

    class Meta:
        database = db


class Task(Model):
    name = CharField(max_length=255)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(rel_model=User, null=True)

    class Meta:
        database = db


# class Context(BaseModel):
#     name = CharField(max_length=255)
#
#
# class ContextTask(BaseModel):
#     context_id = IntegerField()  # foreign key into context
#     task_id = IntegerField()  # foreign key into task
#
#     class Meta:
#         primary_key = CompositeKey(
#             'context_id', 'task_id'
#         )