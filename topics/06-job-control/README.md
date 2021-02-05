# Job Control

  - [MIT Page](https://missing.csail.mit.edu/2020/command-line/) (first half)

Modern operating systems can run multiple programs at once, in fact they rely on
this ability heavily to provide the experience people have come to expect. It
can be helpful to use this ability deliberately (we saw this when we learned how
to use the `parallel` tool) and, at times, this requires that you know how to
manage the running processes on your machine.

```
./job.py A & # Run a job in the background
./job.py B   # Run a job in the foreground
```

We can use `Ctrl-Z` to place the second job ("B") in the background in a
suspended state, this will return us to the shell prompt.

```
jobs
[1]  - running    ./job.py A
[2]  + suspended  ./job.py B
```

We can move "B" back into a running state with `bg`.

```
jobs
[1]  + running    ./job.py A
[2]  - running    ./job.py B
```

Note the "+" and "-". The job marked with "+", generally the last one put into
the background, is the "active" job and will be acted upon by `fg` and `bg` if
they are called with no job ID. The job marked with "-" is the one that will
become active once the current active job finishes.

Note that these jobs continue printing even when they are in the background.
Generally, if you are going to allow something to run in the background you want
to redirect its stdout and stderr.

```
./job.py C &> c_output.txt &
```

Now take a look at the output from job "C": `cat c_output.txt`. You can even do
this in another terminal window since it's just a file.

```
jobs
[1]    running    ./job.py A
[2]  - running    ./job.py B
[3]  + running    ./job.py C &> c_output.txt
```

If we want to bring a job back to the foreground we use the `fg` command. Try
`fg %1` to bring job "A" back up. Now that it's in the foreground we can quit
the program with `Ctrl-C`.

