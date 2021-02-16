# Remote Computing

  - [MIT Page](https://missing.csail.mit.edu/2020/command-line/) (near the end)

Often it is desirable to interact with a computer that isn't sitting on your
desk. Sometimes this means a server of some kind, sommetimes a powerful, shared
computer used for high performance computations, or even an ordinary workstation
to help troubleshoot.

Historically, this was done using a program called
[Telnet](https://en.wikipedia.org/wiki/Telnet). While this protocol is still in
use today, largely as a novelty, a similar, more secure protocol is now in use
called [Secure Shell](https://en.wikipedia.org/wiki/SSH_(Secure_Shell)) or SSH.

As the name suggests, SSH is often used to establish a shell session on a remote
machine. All of the things we have learned previously about using a shell are
still valid, the execution just takes place on a different computer.

SSH is simple to invoke:

```
ssh george@lesica.com
```

The server to which we would like to connect, along with the username are
specified on the command line. In the example above, the username is "george"
and the server is "lesica.com". By default, SSH uses port 22.

It is also possible to specify a command to be run instead of opening a full
shell session. This is handy when you only wish to use the remote computer's
computational resources. Output from the command is delivered back to your local
computer.

```
ssh george@lesica.com ls # Listing of george's home directory
```

## Key-based Authentication

It is possible to avoid typing one's password over and over again. We will walk
through setting up key-based authentication in class and take a look at the
example on the MIT course web page.

## Configuration Options

In addition to key-based authentication, we can also set up "nicknames" for the
servers we connect to most often. This is done using the file `~/.ssh/config`
(create it if it doesn't exist already). This file can be used to set per-server
options. An example is shown below.

```
Host missing
    HostName missing.cs.umt.edu
    User gl219598e
    IdentityFile ~/.ssh/id_rsa_missing
```

This is the entry in my config file for the server we will use in class. Note
that I've nicknamed it "missing", set the username, and pointed it at a key
file. This allows me to connect using a simple command: `ssh missing`.

## Copying Files (scp)

It is possible to copy files to any remote SSH host using the `scp` program.
Since SCP (secure copy) uses the same configuration file, it can be made very
easy to use.

```
scp file.txt missing:/home/gl219598e/
```

There is also a `-r` flag that copies directories recursively, making it easy to
copy a number of files. If you have a lot of data, however, it might be better
to use `tar` to compress the files beforehand.

```
# Use scp directly
scp -r myfiles missing:/home/gl219598e/

# Using tar
tar -cxf files.tar.gz myfiles/
scp files.tar.gz missing:/home/gl219598e/
```

## Tunneling

  - [SSH tunneling tutorial](https://robotmoon.com/ssh-tunnels/)

It is possible to route your computer's network traffic through another machine
using SSH. This can be helpful if you need to access services running on the
remote machine but not exposed to the Internet. It can also allow you to use the
remote machine as a kind of "poor man's" VPN (I used this technique to watch
Hulu when I lived in Chile).

The MIT page has an example and some nice diagrams.

## Tmux

  - [A brief Tmux tutorial](https://danielmiessler.com/study/tmux/)

A terminal multiplexer allows multiple shell sessions to be run and, more
importantly for us, saved and restored. This capability is useful for running a
persistent application on a remote server such that you can return to it later
as though you'd only gotten up from the computer rather than logged out of it.

Tmux and Screen are the most popular terminal multiplexers. Install Tmux using
Homebrew or your Linux distro's package manager.

