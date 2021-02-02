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

Wow, that's a big one.

## Awk

## JSON (jq)

## CSV (csvkit and csvtk)

Comma-separated values files are very common in data analysis. Think of them as
very simple Excel spreadsheets that just hold data and don't do any processing
or calculations. This simplicity is one reason for the popularity of the format,
since CSV files can be read easily on virtually any platform.

We will look at two different tools for working with CSV data on the command
line, but keep in mind that CSV files can also be loaded into ordinary
spreadsheet applications, even Excel!

### csvkit

  - [GitHub](https://github.com/wireservice/csvkit)

### csvtk

  - [GitHub](https://github.com/shenwei356/csvtk)

