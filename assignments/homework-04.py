#!/usr/bin/env python3

# We're going to implement a program that will count occurrences of words in a
# text and print out a table of how many times it found each word. We will
# exclude certain words like "and", "it", "I", as well as any other word with
# fewer than three letters.
#
# You will want to run the program against a large corpus. I suggest "War and
# Peace", which is freely available online
# (<http://www.gutenberg.org/files/2600/2600-0.txt>). You will want to chop off
# the Project Gutenberg header and footer material. This can be done with the
# following command:
#
#     tail -n +835 2600-0.txt | sed -n '/End of the Project Gutenberg EBook/q;p' > tolstoy.txt
#
# See if you can figure out how the command above works. It's kind of dense, but
# it's pretty much all stuff we've learned previously. Once you've run this
# command, you can run the program below against the file tolstoy.txt (it will
# take awhile).

from sys import argv, exit


OUTPUT_THRESHOLD = 10
PUNCUATION = ",.:;?.!'\"“”()[]<>{}"


words = []
counts = []


def update(word):
    word = word.strip(PUNCUATION).lower()

    if len(word) < 3:
        return

    if word in ["and", "the", "for", "had", "who", "not", "too"]:
        return

    if word not in words:
        words.append(word)
        counts.append(0)

    index = words.index(word)
    counts[index] += 1


def tabulate(text):
    for word in text.split():
        update(word)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./homework-04.py <file>")
        exit(1)

    filename = argv[1]
    with open(filename, "r") as infile:
        for line in infile:
            tabulate(line)

    for word, count in zip(words, counts):
        if count < OUTPUT_THRESHOLD:
            continue
        print(f"{word}\t{count}")

