# Cluster and Cloud Computing

While computers have become more powerful over the years, the applications we
expect them to run have grown more complex even faster. As a result, it is often
desirable to spread a computational workload out across a number of machines.

Further, the computational requirements of a given application can fluctuate
dramatically, sometimes even from minute to minute. For this reason, many
organizations find it inefficient to maintain their own hardware and prefer to
rent "cloud" resources.

We will take a quick look at two related practices that facilitate the modern
computing landscape: cluster computing, and cloud computing.

## Cluster Computing

A cluster is, put simply, a collection of computers that operate cooperatively
in some way or another. Clusters are common in scientific applications where
they are used to solve very large mathematical problems that would simply
take too long to complete on an ordinary workstation. But they are also used in
industry to run database systems, game servers, and web applications.

For applications that must keep track of some state, such as direct messages
between users, the use of clusters has motivated a great deal of work in a field
called "distributed systems". For example, if a messaging application server is
run on two computers at once (two "nodes"), then it is important that a new
message be recorded on both of them, regardless of which one initially received
the message from the user's device. It is also important that the message be
recorded only once (you may have noticed unintended duplicates in certain apps).

As it turns out, this is a ferociously difficult problem to solve.
Theoretically, there are a number of good, though sub-optimal, algorithms such
as [Paxos](https://en.wikipedia.org/wiki/Paxos_%28computer_science%29), but
"distributed consensus", as this problem is called, remains difficult in
practice.

### Examples

We will take a tour of one particular application of a high performance
computing cluster and see a cluster in action, including how tasks are
configured and how output is collected upon completion.

## Cloud Computing

Cloud computing, in this context, refers mostly to Infrastructure as a Service
(IaaS) platforms such as Amazon Web Services (AWS). IaaS providers allow
organizations to "rent" virtual hardware for various purposes. Many systems even
allow the creation of entire virtual data centers complete with custom network
topology and firewalls.

The primary advantage IaaS vendors offer is flexibility. It is generally
possible to "spin up" a new machine in a minute or less. This means that as
requirements change, so can computing capability. It is also possible to
assemble an ad hoc cluster this way, which is particularly nice for
organizations that have only infrequent need for massive computing power.

### Examples

We will create a couple cloud servers in class and look at some of the ways they
can be configured. We will also explore some of the other offerings available
through AWS.

