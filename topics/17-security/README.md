# Security

Security is a broad field, so we will cover a smattering of topics that are
likely to be useful to at least many of you.

# Passwords

The most obvious way to handle passwords in an application is to simply store
them somewhere (in a database, perhaps) and when a user attempts to log in, look
up the password that corresponds to the user and verify that it matches.

This actually works just fine, but it has some very unfortunate consequences in
the event that the database where the passwords are stored is compromised since
the attackers get immediate access to all user credentials. Now, you might think
that this isn't a big deal since, if the database has been compromised, the
attackers already have access to every user's data anyway, but, unfortunately,
people tend to re-use passwords across applications. This means that a password
stolen from an inconsequential application might give the attackers access to a
user's email or bank account.

To mitigate this issue, we hash passwords before they are stored. This means
that we apply a one-way function to transform the password into a different
value that can't be easily converted back into the original password. To do
this, we use a "hash function". This is a function `h(x) -> y` with the property
that there exists no (reasonable) function `h'(y) -> x`.

One such hash function is called SHA-256. This is the one we will use in our
examples.

Hashing passwords before storing them goes a long way to fixing the problem
described above, but attackers can still reverse a hash function, at least
probabilistically, using a tool commonly called a Rainbow Table. This is,
essentially, a table of pre-hashed passwords either randomly generated or known
to be in common use. Once such a table has been computed, it is trivial (and
very fast) to convert a hash back into the original password (assuming the hash
exists in the table).

The prevent this, we apply what is known as a "salt" to each password before it
is hashed. Essentially, we take the user's password, add some random data to it
to make it stronger, hash the salted password, and then store the hashed
password along with the salt value in our database. See the pseudo-Python below.

```
def hash_password(pw):
    salt = random_salt()
    salted_pw = pw + salt
    hashed_pw = sha256(salted_pw)
    return (hashed_pw, salt)
```

Now, let's assume that we use a single, randomly chosen, lower-case letter as
the salt value. This means that an effective rainbow table must hash each
password 26 times, once with each possible salt value. This is quite a bit more
work, and makes the table take up quite a bit more space on disk. If we make our
salt values four characters long and allow all alphanumeric characters then a
rainbow table with a given level of effectiveness will be $62^4 = 14,776,336$
times as large. That's already entirely impractical for a table that contains
more than just a few potential passwords.

## Example

Take a look the scripts below and play around with hashing various passwords,
generating rainbow tables, and looking up passwords in those tables.

  * [hash_password.py](hash_password.py)
  * [rainbow_table.py](rainbow_table.py)
  * [table_lookup.py](table_lookup.py)

# SQL Injection



# Buffer Overruns



