# Data Wrangling

  - [MIT Page](https://missing.csail.mit.edu/2020/data-wrangling/)

## Regular Expressions

Regular Expressions let us create patterns that we can match against text. The
simplest possible pattern is just an exact string match. For example, the
pattern `hello` is found within the string "hello world" at position 0.

More complicated patterns can express more interesting matches. For example, the
pattern `[Hh]ello` will match "hello world" as well as "Hello world". We can
also limit matches to the beginning or end of a line, this is sometimes called
"anchoring" the regular expression. The pattern `^hello` will match "hello
world" but not "say hello" because `^` indicates the beginning of the line.

## Sed

  - [Tutorial](https://www.grymoire.com/Unix/Sed.html) - unofficial but good

The command everyone uses Sed for is `s` for substitution. Let's look at an
example. We'll give ourselves a data file and then use Sed to slice and dice it
in different ways. We'll put that in a text file called, shockingly,
`messages.txt`. 

```
2021-01-03 This is a message
2021-01-04 Also a message
2021-01-05 Another day, another message
2021-01-06 Something something message
```

What if we wanted to trim the date off the beginning of each line?

```
cat messages.txt | sed -r 's/^[0-9]{4}-[0-9]{2}-[0-9]{2} //'
```

Breaking this down, we pipe the contents of the file into Sed. Sed is invoked
with the `-r` flag so that we can use regular expressions. Finally, we have a
Sed command that looks for a certain pattern and replaces it with nothing
(`//`), which is the same as removing it.

What if we wanted to transform this file to CSV format and make the year, month,
and day separate columns? That's a little trickier, but really not so difficult
(although we should keep in mind that if our messages have a lot of special
characters the resulting CSV might be invalid).

```
cat messages.txt | sed -E 's/^([0-9]{4})-([0-9]{2})-([0-9]{2}) (.+)$/\1,\2,\3,\4/'
```

Wow, that's a big one. First, we capture four patterns (the parentheses),
excluding the dashes and the space before the message. Then we copy what we
captured, but this time we put commas between the pieces.

Keep in mind that, by default, Sed only operates on the first instance of a
pattern within a line. So the example below will print "goodbye hello".

```
echo "hello hello" | sed 's/hello/goodbye/'
```

If we want to replace all occurrences of a pattern we need to use the `g` (for
"global") flag:

```
echo "hello hello" | sed 's/hello/goodbye/g'
```

We can also use the `-e` command line flag to run multiple Sed commands, one
after the other. For example, what if we weren't sure whether the messages in
the earlier file themselves contained a comma (one of them does, in fact). This
would obviously mess up the formatting of our CSV file. For example, the line

```
2021-01-03 this, is a message
```

would produce

```
2021,01,03,this, is a message
```

which a spreadsheet program might interpret as five columns instead of the four
we intended.

We could deal with this by first replacing commas with `\,` (to escape them) or
even with nothing to remove them.

```
cat messages.txt | sed -E -e 's/,//g' -e 's/^([0-9]{4})-([0-9]{2})-([0-9]{2}) (.+)$/\1,\2,\3,\4/'
```

In this case, we can provide one Sed command for each `-e` and they will be run
in the order they are specified. Note that we could also use another pipe and
run Sed again to get the same behavior, though with a little more typing.

### Insert and append

Read up on the "insert" and "append" commands. These allow lines to be added
above or below lines that match a particular pattern in a file.

## Awk

  - [Tutorial](https://www.grymoire.com/Unix/Awk.html)

Awk is one of those programs that only a few people know how to use properly and
every time the rest of us witness what it can do we vow to learn how to use it.
There's a lot to learn about Awk, however, so it can be daunting. We'll go over
some basics, and if you find yourself inspired to be one of those wizards who
really knows how to use it, you'll be in good shape to continue learning.

First, let's make a CSV file from the output of `ls -l`:

```
ls -l ../../../ | awk '/^[-d]/ {print $6","$7","$3","$9}'
```

Awk has the concept of a "field separator", which it uses to break lines into
pieces automatically. This is handy since a lot of Unix-style program output
ends up formatted at least somewhat like a table. The numerical variables above
(`$6` and so on) refer to fields within a single row (line) of the implied
table.

The regular expression before the opening curly brace (`/^[-d]/`) just tells Awk
to only run on lines that start with either a "-" character or a "d" character.
This is so that we skip the initial line of output ("total 64" in my case).

## JSON (jq)

  - [jq web site](https://stedolan.github.io/jq/)

JSON, or JavaScript Object Notation, is a data serialization format commonly
used to communicate with web services. It is reasonably simple for both machines
and humans to read and write, which makes it a nice compromise compared to more
verbose formats like XML or more efficient ones like MessagePack.

Most common programming languages have some level of support for JSON. Python
includes a JSON package in its standard library. The jq tool allows us to query
and manipulate JSON data from the command line.

Take a look at [reddit.sh](reddit.sh) for an example. We'll go into more detail
during class.

## CSV (csvkit and csvtk)

Comma-separated values files are very common in data analysis. Think of them as
very simple Excel spreadsheets that just hold data and don't do any processing
or calculations. This simplicity is one reason for the popularity of the format,
since CSV files can be read easily on virtually any platform.

We will look at two different tools for working with CSV data on the command
line, but keep in mind that CSV files can also be loaded into ordinary
spreadsheet applications, even Excel!

### csvkit

  - [csvkit on GitHub](https://github.com/wireservice/csvkit)

### csvtk

  - [csvtk on GitHub](https://github.com/shenwei356/csvtk)

