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
