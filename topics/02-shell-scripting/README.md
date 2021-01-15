# Shell Scripting

  - [MIT Page](https://missing.csail.mit.edu/2020/shell-tools/) (first half)
  - [variable.sh](variable.sh)
  - [control.sh](control.sh)

While most shells are themselves fully-featured programming languages, the most
common use of shell scripting to automate or tie together other programs using
relatively simple sequences of commands.

We'll practice writing scripts for a couple different scenarios and think about
how shell scripts can be useful in day-to-day life, even for students.

## Shebang and Preamble

We almost always want to start our scripts with a "shebang" line, which tells
the shell how to execute the script. For example, the line below tells the shell
to use the program located at `/bin/sh` (a simple, but universal shell that
ships with all Unix-like systems) to run the script.

```
#!/bin/sh
```

We can use other programs as well. The shebang line below will run the script
with the user's standard Python 3 interpreter.

```
#!/usr/bin/env python3
```

When we use `/bin/sh` or another, similar, shell, there are options that we can
set to change how the interpreter behaves. One common options is `set -x`, which
causes the script to terminate if any of the commands within it fail.

Putting these things together, a trivially simple script might look like this:

```
#!/bin/sh

set -x

echo hello world
```

## Variables

Variables in shell scripts are used like those in other programming languages,
but there are some differences in syntax and semantics.

```
#!/bin/sh

set -e

# Set a to a string
a="hi there"
echo $a

# This won't do quite what it seems
a="hi   there"
echo $a
```

If we run this code, we get mostly what we expect, but why doesn't the second
version print the extra spaces? That's because variables in shell scripts are
simply interpolated into the script, so `echo $a` becomes `echo hi   there`,
which is a call to `echo` with two arguments. As we know, echo joins its
arguments with a single space and then prints the result.

If we want the extra spaces, we need to wrap the variable in quotes where we use
it so that the shell knows it is supposed to be treated as a single value.

```
a="hi there"
echo "$a"
```

## Control Flow

We have most of the usual stuff here. See `control.sh` for a couple examples. Do
note, however, that the syntax is, as with variable assignment, specific and
inflexible.

## Capturing Output

We can run a command and save its output in two ways. The first is older, and
still often used, but the second is the modern recommendation.

```
files=`ls`
files=$(ls)
```

## Combining Commands

We have a couple constructs that can help us combine commands together to
achieve more complicated outcomes easily.

The double ampersand can be thought of a little like a logical "and" in many
programming languages in that it will "short circuit". The first command to fail
will prevent the rest from running. It can also be used to run a command in a
different directory.

```
<command> && <command>
```

For example:

```
# Run a script inside a specific directory
cd data && ../process_data.py

# Prepare to run a command, then run it,
# if the first step fails, the second step won't happen
./prep_data.py && ./process_data.py
```

The double pipe can be thought of like a logical "or". If the first command
succeeds then the second command will not run because the overall expression is
already "true".

```
<command> || <command>
```

For example:

```
# Prepare some data only if it hasn't already been done
./check_data.py || ./prep_data.py

# Print a custom error if a command fails
./process_data.py || echo "failed to process data"
```

