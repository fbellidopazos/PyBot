import sqlite3

db=sqlite3.connect("Users.db")
db.execute("create table Users(Name text,Nick text,Main_Role text)")