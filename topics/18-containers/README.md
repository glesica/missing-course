# Containers

  - [Linux Containers](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
  - [Docker](https://www.docker.com)
  - [Podman](https://podman.io)

Containers are all the rage lately, and perhaps for good reason. A container is
similar to a virtual machine in that it provides an isolated environment in
which one or more applications may be run. Unlike a virtual machine, however,
programs run natively inside of a container, no machine emulation is required.

Two popular container runtimes are [Docker](https://www.docker.com) and
[Podman](https://podman.io). These provide a UI layer over the top of
capabilities provided by the Linux kernel.

Containers have a variety of use-cases, we will discuss a couple of them in
class and look at some examples.

## Isolated Environment

Containers can provide us with an isolated, reproducible environment for
building or testing software. For example, building a particular program may
require that certain libraries, or even certain versions of those libraries,
exist on the machine.

Ordinarily, this would pose challenges. One developer might use Fedora Linux,
another Ubuntu Linux, and still a third macOS. Containers allow us to construct
an operating system image that already has everything needed by the software so
that we don't have to figure out how to create the appropriate environment
across all three of these platforms.

Often, containers like this can even be reused by CI systems so that the build
artifacts produced by the CI system exactly match those that would be produced
by developer workstations.

Take a look at the Dockerfile in the root of the course web site repository for
an example of a container used in this manner.

## Application Distribution

Have you ever tried to run a Python application only to discover that you had
the wrong version of Python installed, or that you were missing some required
library?

Containers provide a solution to this problem by encapsulating not just the
program being run, but its entire runtime environment. This can be especially
handy for software that relies on a niche (a less popular programming language,
for example) or highly specific (Python 2.7, for example) runtime.

A container can also be configured to include data or other support files
required by an application to avoid requiring the user to provide these.

## Modular Infrastructure

Containers can also be used as servers to simplify configuration and scaling.
For example, a container can be constructed to run a web application server,
allowing one or more copies, even different versions, to run on the same
physical (or virtual) hardware.

