#!/bin/sh

# List all of the ".sh" files under the current directory or any of it
# subdirectories (recursively). For example, `myscript.sh` and
# `folder/otherscript.sh` should both be included. Hint: you can do this easily
# using the `ls` and `grep` commands.

ls | grep ".sh"
or it's
ls | grep -r ".sh"


# Count how many ".zip" files there are in the current directory. Your command
# should output only a numerical value, nothing else. Hint: one way to do this
# involves two "pipes" (`|`) and the `wc` command. It is also possible, though
# quite verbose, to do this with a `for` loop.

ls | grep ".zip" | wc -l

# Imagine that you have a bunch of source code files with ".py" file extensions.
# We want to find all the lines in these files that define new functions (they
# contain the `def` keyword). We want to print the contents of each line, plus
# the filename and line number. There are a bunch of ways to do this, some
# simpler than others.

files="ls | egrep '.py|def' *.py"
for entry in $files
do
    echo $entry
    grep -hn $entry
done


or would the following work since its all python files?

files="ls | egrep 'def' *.py"
for entry in $files
do
    echo $entry
    grep -hn $entry
done
