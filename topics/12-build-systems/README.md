# Build Systems

  - [MIT Page](https://missing.csail.mit.edu/2020/metaprogramming/) (Build
    Systems)

When programs are small, particularly when they fit in a single file, it is
perfectly acceptable to simply invoke the compiler or interpreter directly.
However, as programs grow in size it is helpful to add a bit more structure.

## Make

  - [GNU Make](https://www.gnu.org/software/make/)
  - [An unofficial tutorial](https://makefiletutorial.com)
  - [Automatic variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html)

Make is a tool for building files based on the contents of other files. At its
core, this is pretty much what we do as programmers, so Make is a pretty useful
tool for us!

Make is based on the concept of targets and prerequisites. A target is something
that can be built, and prerequisites are the building blocks out of which the
target may be constructed. Take a look in the [example-make/](example-make/)
directory for a Makefile that resizes images. We will go over this file in
class.

## Go Toolchain

  - [Go programming language](http://golang.org)

It is becoming common for modern programming languages to ship a build system
alongside the compiler / interpreter. A good example of this is the Go
programming language, which includes an efficient build system.

Take a look at [example-go](example-go/) for a tiny Go project and some
instructions for building it.

## Case Studies

We will take a look at a couple of real-world examples in class. They are
briefly described below.

### Webpage

For a nice example of a Makefile, let's take a look at
<https://github.com/glesica/webpage>. This is a minimalist system for creating a
static web site. It relies on a Makefile to build a collection of Markdown
documents into a functioning web site. We will look at the Makefile during
lecture.

