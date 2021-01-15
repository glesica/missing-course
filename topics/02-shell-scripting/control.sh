#!/bin/sh

set -e

greeting=$1
other=$2

if [ "$greeting" = "hello" ]; then
    echo "hello to you as well"
fi

names="bob anne pete"
for i in $names; do
    echo "there is a file $i"
done

addsomething() {
    local value=$1
    echo $(($value + $other))
}

addsomething 5
echo $value

