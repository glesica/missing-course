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

```python
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

SQL injection is a common attack used against applications that store their data
in a SQL database. It works by tricking a program into inserting code into a SQL
statement instead of just data.

![Exploits of a Mom (xkcd)](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

For example, in the famous cartoon above, the child's name contains SQL code
that is designed in such a way that it is likely to be syntactically valid when
directly interpolated into a SQL query, but when it is run it attempts to delete
the database table called "Students".

The reason this sort of thing works is that we build up SQL code inside of our
programs, then execute that code on the fly. The same thing would be possible
with ordinary programming languages if we created code on the fly. In fact, many
languages have the ability to evaluate snippets of their own code, but doing so
is generally considered a bad idea because it can leave a program open to
similar injection attacks. For example, Python supports this through the `eval`
function:

```python
eval("print('hello')")
```

Typically, SQL injection is prevented by correctly parameterizing queries.
Different database client libraries for different programming languages may use
different syntax for doing this, but most provide similar capabilities. For
exampe, the query below is vulnerable to injection:

```python
cursor.execute("SELECT * FROM users WHERE name='%s'" % name)
```

On the other hand, this query is not, because it substitutes the name into the
query using the SQL library as opposed to simple string interpolation:

```python
cursor.execute("SELECT * FROM users WHERE name=?", (name,))
```

A good rule of thumb is to never include user input in code that will be run on
the fly unless it has been properly escaped / sanitized. Also keep in mind that
this isn't something you want to try to do yourself because it is easy to forget
an edge case and leave your program open to injection attacks.

## Example

Take a look at [user-lookup.py](user-lookup.py) for an example. This script
accepts a user name and a password and prints a secret word, specific to that
user, if the password is correct.

The first time it is run it will create a database file called `users.db`. You
can reset the database by deleting the file. You can also interact with the
database directly using the `sqlite3` tool, if you have it installed.

```
./user-lookup.py Travis changeme
```

If you enter the wrong password, however, you'll get back an error message
instead of the super secret word.

Try running it for "George" as well (his password is "sosecure"). As you can
see, George and Travis have different secrets.

Now, let's inject some SQL into the program by running the script like this:

```
./user-lookup.py George "' OR password <> '"
```

What happened? Why did it produce that result? How did it give us George's
secret without the correct password?

# Buffer Overruns

A buffer overrun occurs when a program reads memory beyond the end of an array.
This is impossible to do in most languages, but it can happen in languages like
C that allow direct access to memory and, in particular, pointer arithmetic.

Pointer arithmetic is basically what it sounds like. A pointer is just an
address in memory, which means that it is an integer since "memory" is
essentially just a linear array of bytes (see below).

![Memory Layout](media/17-memory-layout.png)

In C, an integer can be used as a pointer, and a pointer can be used as an
integer, they are essentially the same thing. Therefore, pointers can be
added and subtracted. This means that if I have a pointer to a particular memory
location, let's say `0xFF56`, I can add one to it and now I have a pointer to
the memory location `0xFF57`. Now, if I dereference this pointer, I get whatever
data happens to be stored at `0xFF57`.

In fact, this is essentially how arrays work in C. The syntax `myArray[5]` is
actually just shorthand for something like:

```c
*(myArray + 5)
```

As you might guess, then, an array variable in C is very similar to a pointer to
the first element (the reality is a little more complicated, but it's a
reasonable approximation). However, this means that there is no way for the
computer to know how long you expect a given array to be, it knows where the
array starts and not much else.

Because of everything described above, it is possible to read beyond the end of
an array. The result of doing so depends on what is (or was) stored adjacent to
the array data. An attacker can use a buffer overrun bug to attempt to access
sensitive data, like encryption keys.

## Example

The file `secrets.c` contains a program that loads secrets and names into memory
and then provides access to the names by index. For example, `./secrets 0`
prints "George" because that is the first value stored in the `names` array.
However, if we run `./secrets 2` we get a surprise. Instead of a name (or an
error message), we get one of the secret values!

You can build the program by running `gcc -o secrets secrets.c`, assuming you
have the GCC C compiler installed.

