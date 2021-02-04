#!/bin/sh

set -e

REDDIT_FILE=reddit.json

# Grab the front page of reddit if we haven't already done so. Doing the
# download this way keeps us from hitting a rate limit on requests to the Reddit
# API if we run the script repeatedly for debugging.

if [[ ! -f "$REDDIT_FILE" ]]; then
    curl -A 'curling is fun' -o "$REDDIT_FILE" https://www.reddit.com/.json
fi

# Now we can cat the file and treat the output as though it was coming directly
# from Reddit using curl. Let's pipe the file directly into jq to see what
# happens. By default, jq will "pretty print" JSON data for us, including
# formatting and syntax highlighting. This feature alone is worth the price of
# admission for people who work with JSON data regularly.

cat "$REDDIT_FILE" | jq

# Let's give ourselves a project. We want to print a list of the top stories on
# a given Subreddit, or on the front page by default, and then print their
# titles and associated URLs. Note that I've broken this up into several
# invocations of jq to make it easier to read, we could just as easily have used
# jq's internal pipe operator.

cat reddit.json \
    | jq '.data.children[]' \
    | jq '{title: .data.title, url: .data.url}' \
    | jq '.title, .url, ""' \
    | sed 's/"//g'

