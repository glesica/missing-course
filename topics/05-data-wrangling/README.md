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

## CSV (csvkit)

Comma-separated values files are very common in data analysis. Think of them as
very simple Excel spreadsheets that just hold data and don't do any processing
or calculations. This simplicity is one reason for the popularity of the format,
since CSV files can be read easily on virtually any platform.

### Project

In order to make this more interesting, we will play around with some real CSV
files. The first contains
[house sale data](https://www.kaggle.com/harlfoxem/housesalesprediction)
from King County, WA (which includes Seattle). This spreadsheet contains sale
price, zip code, and some characteristics of each house sold during a
particular time period. The second contains various
[tax statistics](https://www.kaggle.com/irs/individual-income-tax-statistics)
and happens to also contain zip codes, which we will use later.

### csvkit

  - [GitHub Page](https://github.com/wireservice/csvkit)

CSVKit actually consists of several command line utilities, each with a specific
purpose and its own set command line flags.

The `csvstat` tool gives us summary statistics (average, and so on) for each
column in the spreadsheet. This can be a handy place to start when working with
unfamiliar data. It can also hint at errors in the data. Two examples are shown
below.

```
csvstat kc_house_data.csv

...

  2. "date"

        Type of data:          DateTime
        Contains null values:  False
        Unique values:         372
        Smallest value:        2014-05-02 00:00:00
        Largest value:         2015-05-27 00:00:00
        Most common values:    2014-06-23 00:00:00 (142x)
                               2014-06-26 00:00:00 (131x)
                               2014-06-25 00:00:00 (131x)
                               2014-07-08 00:00:00 (127x)
                               2015-04-27 00:00:00 (126x)

  3. "price"

        Type of data:          Number
        Contains null values:  False
        Unique values:         4028
        Smallest value:        75,000
        Largest value:         7,700,000
        Sum:                   11,672,925,008
        Mean:                  540,088.142
        Median:                450,000
        StDev:                 367,127.196
        Most common values:    450,000 (172x)
                               350,000 (172x)
                               550,000 (159x)
                               500,000 (152x)
                               425,000 (150x)

...
```

The `csvcut` tool can extract and filter columns from a file. The first thing
we'll do is run `csvcut -n` on one of our files to display the column headers
(names).

```
csvcut -n kc_house_data.csv
  1: id
  2: date
  3: price
  4: bedrooms
  5: bathrooms
  6: sqft_living
  7: sqft_lot
  8: floors
  9: waterfront
 10: view
 11: condition
 12: grade
 13: sqft_above
 14: sqft_basement
 15: yr_built
 16: yr_renovated
 17: zipcode
 18: lat
 19: long
 20: sqft_living15
 21: sqft_lot15
 ```
 
Now we can choose the columns we want to use and pull them into a separate file
to make things easier to work with. Check out [simple_csv.sh](simple_csv.sh) to
see how this is done.

Now let's turn our attention to the tax data. The column names here are hard to
interpret, so I'm gone ahead and picked out a couple for us to use. When we
transform the CSV file we will also rename these columns.

| Old Name | New Name           |
| -------- | --------           |
| a02650   | total_income       |
| n02650   | total_income_count |
| numdep   | dependent_count    |
| zipcode  | zipcode            |

Unfortunately, CSVKit doesn't have a fancy command to rename columns, but we can
easily use a tool we already learned about: Sed! Check out the script to see one
way of doing this.

Finally, we're going to join these two datasets together. Why is this useful?
Well, imagine we have a theory that, say, more expensive homes in certain
markets tend to be owned by people who earn money through passive investments as
opposed to participation in the labor market. This is a bit of a hot button
issue right now as people in many desirable real estate markets have begun to
feel "priced out". Providing evidence for a theory like this will almost always
require data from more than one source, so being able to stitch CSV files
together can be quite valuable.

To do this, we use the `csvjoin` tool. We can specify the column to join on
using the `-c` option, giving it either a single column name (`zipcode`) or a
comma-delimited list of two names if the files use different names
(`zipcode,zip_code`, for example).

## Producer / Consumer Pattern

We've used a lot of pipes (`|`) so far, but aside from the fact that they work
by sending the output of one command into the next command as its input, we
don't know much about them. So let's think about a particular software
development pattern and use it to experiment a little with how pipes actually
work.

It is very common to have a program that produces data, perhaps directly or
perhaps in response to some kind of user or external (like a sensor) input. This
sort of program is known as a "producer". It is also common to have a program
that accepts data and processes it in some way. If we plug a producer into a
program like this then we call it a "consumer" because it consumes the data
produced by the producer. Producers and consumers can be independent programs or
they can be logical parts of a single program, like functions or classes.

We'll use the [produce.py](produce.py) and [consume.py](consume.py) scripts and
run them as a pipeline as an example. This will also give us a chance to see how
pipes work.

