# CPU Profiling

  - [MIT Page](https://missing.csail.mit.edu/2020/debugging-profiling/)

CPU profiling is the practice of measuring how much "work" the computer is doing
when it runs your code, and which parts of your code require the most work. In
most cases, we measure "work" using the amount of time something takes, but this
is not universal.

CPU profiling is a kind of "dynamic analysis", because it requires running the
code in question.

We will look at some simple profiles for toy programs and then dive into a real
codebase.

## Small Example

Take a look at [factorize.py](factorize.py) to see the code we're going to
profile. It isn't very complicated and, honestly, in real life we shouldn't need
a profiler here. But the goal is to learn how to interpret a profiler's output,
not improve the code.

Note that this example uses the [Pipenv](https://pipenv.pypa.io/en/latest/)
tool, which can be installed quite easily on most systems. This provides us with
a consistent environment for installing Scalene (see below) and
[Pytest](https://docs.pytest.org/en/stable/) (for running the doctests).

### cProfile

This profiler ships with Python itself. It provides a great deal of information
but its user interface is minimal.

```
pipenv run python -m cProfile factorize.py 23587984332346347
```

### Scalene

Scalene is an alternative profiler that also supports memory profiling. Its user
interface is a bit more friendly than cProfile and it can output nicely
formatted HTML.

```
pipenv run scalene --cpu-only factorize.py 23587984332346347
```

## Real World Example

We will take a look at a real Python codebase in class.

