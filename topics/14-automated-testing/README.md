# Automated Testing

Everyone who has ever learned to program has also learned to test software. When
you wrote your first "Hello, world!" you tested it. You compiled it, ran it, and
verified that it printed the famous phrase. But when programs get large, as they
tend to do, we need additional tools and practices to ensure that they do what
we want them to do.

This is where automated testing comes in.

## Assertions

Testing is essentially the process of verifying that, for a given set of inputs,
your program produces the correct outputs. Sometimes we have a get a little
fuzzy with our definition of "correct", but at the end of the day that's pretty
much it.

In order to verify a correct output we make an assertion about it. For example,
to test a function that adds two numbers together, we might *assert* that for
the inputs `2` and `3`, the output is `5`. When an assertion is violated, then
we have a test failure.

I said earlier that "correct" can end up being a fuzzy concept. As an example,
let's say we have a program that, when run, simulates rolling one or more dice,
with two or more "sides" each.

```
./rolldice 2 6
```

The command above, then, would roll two dice, each with six sides. We can't
verify the correctness of this program by asserting exactly which numbers will
print out when it is run, because they're random. So how do we define "correct"?

We have a couple options:

  1. Verify that two outputs are produced
  2. Assert that each output is between one and the number of sides
  3. Verify that, on rolling the dice 1,000 times, we get each value
     between one and the number of sides at least once
  4. Statistically verify that, on rolling the dice 1,000 times, we get each
     value between one and the number of sides `1/N` times where `N` is the
     number of sides
  5. Verify that the program completes successfully (doesn't crash or print an
     error message) for many values of each of the parameters
  6. Perform a parameter sweep on both the number of dice and number of sides
     and verify that the program completes successfully for each combination

There are probably others as well. But how do we choose? Well, it depends on
what we're trying to accomplish with our tests, how long we are willing to wait
for the tests to complete, and how much effort we wish to put into writing and
maintaining the tests themselves.

Testing is a bit of an art.

## Test Cases

Let's say you've got a program you want to test and you've decided what it means
for a particular set of outputs to be "correct" given a particular set of
inputs. How do you know which inputs to use in your tests?

This can be, again, a bit of an art, but there are some general guidelines we
can use.

Always attempt to test boundary values. A boundary value is one that occurs on
or near a boundary between two parts of a value's domain. For example, `-1`,
`0`, and `1` are boundary values for signed integers. The reason for this is
that negative and positive integers often behave differently under common
mathematical operators, and zero behaves differently from either of them. For
example, say you have the expression `r = q / n` in your code:

  - if `n` is zero, then your program might crash
  - if `n` is positive, then `r` will have the same sign as `q`
  - if `n` is negative, then `r` will have the opposite sign as `q`
  - if `q` is zero then `r` will be zero and we need to worry about using it as
    a denominator elsewhere

So, in choosing values to test, we probably want to make sure `n` takes on
negative, positive, and zero values, and that `q` ends up being zero at some
point.

Another piece of advice is to always test the absence of data, if it can
possibly occur. This often means testing what happens when a variable is `null`
or `nil` (or whatever a given language calls it). With strings and collections
(like lists), this usually means testing the "empty" version of these data
structures.

Finally, testing extreme values can be handy for various reasons. For example,
if you define a function that accepts a signed 32 bit integer, test a value
(one that makes sense given your algorithm) that is close to the minimum and
maximum representable values for this type, around +/- 2 billion. Note, however,
that this could also be seen as a special kind of boundary value since values
larger than $2^32-1$ "roll over" and become negative.

## Functional Testing

Functional testing attempts to test the functionality, or behavior of a piece of
software. This is what we all did when we run our first programs and verified
that they'd printed "Hello, world!".

At a basic level, functional testing ensures that users get what they expect out
of our software. If a program won't even run, for example, then it isn't useful
to anyone.

Automated functional tests can be tedious to set up, particular for graphical
applications where we must somehow simulate a mouse and keyboard. There are many
tools available that make this process easier, however. For web-based
applications, [Selenium](https://www.selenium.dev) and
[Puppeteer](https://pptr.dev) provide interfaces for automating popular web
browsers. We will take a look at Selenium in class.

## Unit Testing

Unit testing attempts to verify the whole by verifying the individual parts. A
"unit" in this case is a smaller piece of a program, such as a function or
class. The advantage here is that the tests are often easier to write since a
single function is usually a lot simpler than an entire program.

Consider the following function, along with its doctests (which are a style of
writing unit tests popularized by Python but adopted by other languages as
well):

```python
def pad_left(s: str, n: int):
    """
    Pad s on the left to have at least length n.
    
    >>> pad_left("a", 2)
    ' a'
    >>> pad_left("aaa", 2)
    'aaa'
    """
    pass
```

The tests verify that the function works, but say nothing about a larger program
that might be built with this function.

Unit tests are also widely used in re-usable code libraries to ensure the
correctness of the algorithms within the library without the need for a "driver"
program. This also means that developers using a particular library can
generally assume that the library's code is correct, reducing their own testing
burden.

