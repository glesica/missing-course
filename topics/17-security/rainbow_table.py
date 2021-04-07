#!/usr/bin/env python3

# Usage:
# ./rainbow_table.py [MAX_LENGTH, [SALT]]
# Create a rainbow table consisting of all possible passwords with MAX_LENGTH or
# fewer characters (a-z). If SALT is given, then apply it to each password.

from hashlib import sha256
from sys import argv

if len(argv) > 1:
    MAX_LENGTH = argv[1]
else:
    MAX_LENGTH = 4

if len(argv) > 2:
    SALT = argv[2]
else:
    SALT = ""

# We assume that the password consists only of lower-case ASCII characters. This
# is just for simplicity.

CHARS = [chr(i) for i in range(97, 123)]

def passwords(chars, length, prefix = ""):
    yield prefix + SALT

    if length == 0:
        return

    for c in chars:
        for pw in passwords(chars, length - 1, prefix + c):
            yield pw + SALT

def hash_password(password):
    salted_password = password + salt
    return sha256(salted_password.encode()).hexdigest()

for pw in passwords(CHARS, MAX_LENGTH):
    hashed_pw = hash_password(pw)
    print(f"{hashed_pw} {pw}")

