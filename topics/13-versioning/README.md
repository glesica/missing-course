# Versioning

  - [MIT Page](https://missing.csail.mit.edu/2020/metaprogramming/) (Dependency
    Management)

Programs that we use every day usually have simple, if sometimes silly, version
numbers like Chrome 88, or PyCharm 2020.3, or Ubuntu 20.10. They sometimes
express the year and month of release, but ultimately they simply mark the
passage of time. These versions are intended for human and marketing
consumption. 

Libraries, on the other hand, need "smarter" versions. As an example, say we
have a Python math library with the following functions:

```python
def square(n):
    return n * n

def triple(n):
    return n + n + n
```

Now, perhaps, we create a program that relies on this library and we use both of
these functions:

```python
a = math.square(5)
b = math.triple(5)
print(a > b)
```

This is great, but what happens if the authors of the library release a new
version?

```python
def square(n):
    return n * n

def triple_it(n):
    return n * 3
```

Do you see the problem? Our program will crash because it can't find the
`triple` function (which has been renamed `triple_it`):

```
AttributeError: module 'math' has no attribute 'triple'
```

What we need is a way to predict whether a new version of the library is "safe"
for us to use in our program.

For this, it is common to use a practice called Semantic Versioning.

## Semantic Versioning

  - [Semantic Versioning](http://semver.org)

Simply put, Semantic Versioning allows library authors to express what about
their libraries has changed from one version to the next for purposes of
ensuring compatibility.

At its most basic level, a semantic version consists a three numbers, separated
by periods. For example, `3.17.8`. The first portion is the "major" version
number, the second is the "minor", and the third is the "patch".

Semantic versioning gives us rules about when to increment each number. If a
library breaks compatibility, as we saw in the example above, it should
increment the major, and reset the minor and patch to zero. For example, `1.4.3`
might become `2.0.0`.

If a new version adds new features, but does not remove any existing features or
otherwise break compatibility, then the minor version increments. For example,
`1.4.3` might become `1.5.0`.

Finally, if a new release contains only bug fixes and doesn't add anything new
or remove anything that already existed, then the patch is incremented. So
`1.4.3` would become `1.4.4`.

We will work through some examples in class and then check out some tools that
can take advantage of semantic versioning to keep our libraries up to date
safely.

