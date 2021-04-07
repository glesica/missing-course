#!/usr/bin/env python3

# Usage:
# ./hash_password.py <PASSWORD> [SALT]
# Hash the given PASSWORD, optionally applying a SALT value.

from hashlib import sha256
from sys import argv

password = argv[1]

if len(argv) > 2:
    salt = argv[2]
else:
    salt = ""

# We "salt" the password by appending the salt value to the end of the password.
# This isn't particularly interesting, and it doesn't need to be.
salted_password = password + salt

# Python requires us to convert from a Unicode string to a "byte" string since
# the hash algorithms operate on bytes, not Unicode characters (which can
# consist of multiple bytes each).
bytes_value = (salted_password).encode()

# This is where we apply the hash function. We request the hex digest, which is
# just the hash value printed as a hexidecimal string (since not all bytes in
# the hash value have ordinary character representations).
hash_value = sha256(bytes_value).hexdigest()

if salt:
    print(f"{hash_value} {salt}")
else:
    print(hash_value)

