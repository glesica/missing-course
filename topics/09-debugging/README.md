# Debugging

  - [MIT Page](https://missing.csail.mit.edu/2020/debugging-profiling/)

Debugging is a big topic. There are many debugging strategies and tools and we
will only cover a couple of them here.

## Print

The simplest debugging strategy, and probably the first one we all used, is to
simply print one or more values and see if they are what you expected them to
be.

```python
def my_algorithm(a):
    # print(f"a = {a}")
    b = step1(a)
    # print(f"b = {b}")
    c = step2(a, b)
    # print(f"c = {c}")
    d, e = step3(a, c)
    # print(f"d = {d}, e = {e}")
    f = step4(a, d, e)
    # print(f"f = {f}")
    return f
```

## Debugger

A debugger is a program that "wraps" your program and allows you to do things
like pause execution and inspect your program's internal state. Debuggers exist
for many programming environments, but we will look at examples using C++ and
Python codebases.

