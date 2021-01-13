# Shell Scripting

  - [MIT Page](https://missing.csail.mit.edu/2020/shell-tools/) (first half)

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

## Control Flow

## Capturing Output

