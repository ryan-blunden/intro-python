#!/usr/bin/env python3
import records
import requests

# randomuser.me generates random user data
users_json = requests.get('http://api.randomuser.me/0.6/?nat=us&results=10').json()['results']

db = records.Database('sqlite:///users.db')

db.query('DROP TABLE IF EXISTS users')
db.query('CREATE TABLE users (key int PRIMARY KEY, first_name text, last_name text, email text)')

for rec in j:
    user = rec['user']
    name = user['name']

    key = user['registered']
    fname = name['first']
    lname = name['last']
    email = user['email']
    db.query('INSERT INTO persons (key, fname, lname, email) VALUES(:key, :fname, :lname, :email)',
             key=key, fname=fname, lname=lname, email=email)

rows = db.query('SELECT * FROM persons')
print(rows.export('csv'))
