# Homework 9

The domain of a hash function is generally larger than its range. This is
because most hash functions produce output of a certain size, but can accept
input of any size. For example, it is possible to hash the contents of "War and
Peace" using the SHA-256 algorithm, but the value it produces will still be 256
bits (much shorter than the book).

This means, by definition, that there exists at least one pair of inputs, $x_1$
and $x_2$ such that, for a given hash algorithm $h$, $x_1 \ne x_2$ and
$h(x_1) = h(x_2)$. In other words, the two values, though they are different, share
the same hash value.

This is commonly referred to as a "collision". The implication for password
hashing is that if two passwords collide, then they are indistiguishable and if
one of them grants the user access, the other will too.

For this reason, it is important to use good, cryptographically sound hash
algorithms for passwords. The code below implements an unsound (in fact
laughably so) hash algorithm, though the output looks, at least superficially,
realistic.

```python
def dumb_hash(pw: str) -> str:
    h = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    for c in pw:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            h[i] += ord(c)
        elif c in "abcdefghijklmnopqrstuvwxyz":
            h[i] += ord(c) * 2
        else:
            h[i] += ord(c) * 4
        
        i = (i + 1) % len(h)

    digest = ""
    for v in h:
        digest += hex(0x1000 + v)[2:6]

    return digest
```

You can also download the code: [dumb_hash.py](dumb_hash.py).

Analyze the code above and find two passwords that will hash to the same value
(collide). Submit both of them, along with their hash value. You don't need to
submit anything else.

You may need to look up what the `hex` and `ord` functions do, in particular.
You should also probably place the code in a script so that you can run it to
check your work.

## Example Solution

Below is an example solution, including an explanation. This is the kind of
"bug" in the algorithm that you should attempt to find. Obviously, you can't
submit the answer below, but don't worry, there are many more like it!

  > Two passwords that hash to the same location are 11111111 and bbbbbbbb,
  > and their hash is 10c410c410c410c410c410c410c410c4.
  >
  > This is because the Unicode representation for "1" is 49, and the
  > Unicode representation for "b" is 98. The function uses 49 x 4
  > for 1 since it is in the "else" category, and 98 x 2 for b since
  > it is in the lowercase category, and these both equal 196.

