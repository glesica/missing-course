#!/usr/bin/env python3

from os import path
import sqlite3
from sys import argv

# Usage:
# ./user-lookup.py <USER> <PASSWORD>
# Look up the secret word for the given user, assuming the given password is
# correct. Reset the database by deleting the file "users.db".

DB_FILE = "users.db"

if not path.exists(DB_FILE):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    cur.executescript("""
CREATE TABLE users (name text, password text, secret text);
INSERT INTO users VALUES
    ("George", "sosecure", "Mississippi"),
    ("Travis", "changeme", "Kansas");
    """)

con = sqlite3.connect(DB_FILE)
cur = con.cursor()

user_name = argv[1]
password = argv[2]

cur.execute(f"""
SELECT secret FROM users
WHERE name='{user_name}' AND password='{password}'
""")

row = cur.fetchone()
if row:
    secret = row[0]
    print(f"Secret: {secret}")
else:
    print("User not found")

