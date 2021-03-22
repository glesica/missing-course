# Homework 7

  * [parse_math.py](../topics/14-automated-testing/parse_math.py)

Implement the `parse_math` in the file linked above. We wrote tests for this
function in class. Use the unit tests to guide your implementation and keep in
mind that all of the tests we wrote need to pass in order for your code to be
considered correct.

Submit your implementation on Moodle.

## Run the tests

You can run the doctests from the command line using the
[Pytest](https://docs.pytest.org/en/stable/) tool.

```
pytest --doctest-modules parse_math.py
```

## Hints

Remember that passing the tests is a necessary, but not sufficient condition to
demonstrate program correctness. Keep an eye out for situations not covered by
the tests and feel free to add test cases.

You will likely want to process one character at a time. Parsers are often
written to be "stateful". This means that as you process an additional character
you decide how to treat that character based on the characters you've seen
previously.

For example, operands can consist of more than one character. This means that
when we come upon a digit we can't just assume that's the entire operand and
convert it to an int, we have to wait to see if the integer has additional
digits.

By the same token (get it?), when we run into an operator, we know that we can
process it immediately, but we may have already been in the midst of processing
a multi-character operand, so we have to close out any existing operand
processing (convert the characters to an integer) before we can handle the
operator.

