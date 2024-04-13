from peewee import PostgresqlDatabase
from dotenv import load_dotenv
from peewee import SqliteDatabase
import os


load_dotenv()

db = PostgresqlDatabase(os.getenv('DATABASE_URI', ''))

#db = SqliteDatabase('dbseatools.db')