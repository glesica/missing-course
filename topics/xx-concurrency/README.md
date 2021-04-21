# Concurrency and Parallelism

Concurrency is, conceptually, the pursuit of multiple goals or tasks at one
time. You can think of this like multi-tasking (the metaphor is actually pretty
accurate, which helps explain why people don't multi-task very well).
Concurrency does not, however, necessarily mean that more than one goal or task
can advance at the same moment in time.

When multiple things happen at the same moment in time, then we have
parallelism. The difference here can be subtle, but it is vitally important. For
example, let's say we have two computations, `A` and `B` that take 10s and 20s,
respectively, to run on a given computer. If we run them concurrently, but not
in parallel, then they will take 30s to finish. However, if we run them
concurrently and in parallel, they will take 20s to finish.

## Concurrency

If concurrency does not imply parallelism, then why does it matter? There are
several potential benefits to concurrency, even in the absence of parallelism,
depending on the properties of the system in question. Most of these benefits
fall into one (or both) of two categories: responsiveness and intermediate
results.

### Responsiveness

When two (or more) processes run concurrently they can take turns making
progress. One can pause while the other runs, and then they can swap. This
implies that we can assign higher or lower priority to different processes at
different times. This is particularly valuable for user interfaces, where we
want the buttons and scroll bars and such to remain responsive, even though
other things may be happening as well.

To achieve this, we prioritize the process that accepts and handles user input
so that when there is UI work to be done, it is done right away. In fact, early
GUI systems didn't do this and, as a result, gained a reputation for being
frustrating to use.

### Intermediate Results

Often, our computations don't have just a single output. They often produce many
results (such as an array of values) or they may be able to issue status updates
as they run (like updating a progress bar).

Concurrency gives us the opportunity to make partial progress on more than one
task and, in some cases, allows tasks to cooperate or be terminated early if
this is desired.

For example, we might have two processes, one that fetches data from a network
service and another that calculates some statistics on the data and writes the
results to a file. In this case, without concurrency, the first process would
have to finish its entire download (which could be quite large) before any
further processing could occur. So if the fetch process takes 30s (total) and
the statistics process takes 12s (total) we would have to wait 42s before we saw
any results at all. On the other hand, if we can allow the fetch to run
partially, perhaps for 5s at a time, followed by the statistics process, which
would take about 2s at a time since we're talking about 1/6 of the total data,
we could see partial results after only 7s.

## Parallelism

Ultimately, once you understand the idea behind concurrency, parallelism is
fairly straightforward since it is just concurrency where multiple tasks can be
run simultaneously. That is not to suggest that it is always easy to take
advantage of parallelism, of course, which can be quite tricky to get right.

## Example

See [workers.py](workers.py) for an example of concurrency / parallelism using
Python. This is a convenient language to use since it is very easy to switch
between only concurrency and concurrency with parallelism.

