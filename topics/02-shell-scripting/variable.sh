#!/bin/sh

set -e

# Set a to a string
a="hi there"
echo $a

# This won't do quite what it seems
a="hi   there"
echo $a

