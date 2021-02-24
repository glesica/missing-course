# Version Control

  - [MIT Page](https://missing.csail.mit.edu/2020/version-control/)

In the before times, people used all kinds of tricks to keep track of changes
they made to documents or code. Some people named files and directories with
numbers, like `file 1.docx`, `file 2.docx`, and so on. Eventually, this would
devolve into utter chaos, like `file 2 final.docx` or `file 2 final 2.docx`! 

Another strategy, for code, was to comment out old code in favor of newer code.
For example:

```python
def fancy_algorithm():
    # old version
    # if something:
    #     do_another()
    #     then_this()
    
    # new version
    if something and other_thing():
        do_this_thing()
        do_another_thing()
```

This is pretty insane, because eventually the code becomes littered with dead
code and no one can remember where it came from or what it did.

Thankfully, it has become commonplace to use a version control system, at least
for source code if not for other documents as well (this web site is under
version control, for example). A very popular system today is
[Git](https://git-scm.com), which was originally built for the Linux kernel
project. We will learn the basics of Git, the MIT page has a good tutorial and
there are countless alternative tutorials online.

In class, we're going to take a look at some standard workflows as well as some
less common tasks.

  - Create a repository
  - Add files
  - Make a commit
  - Modify files
  - Undo changes to files
  - The stash
  - Create a branch
  - Merge a branch
  - Resolve a merge conflict
  - Create a repository (GitHub)
  - Add a remote
  - Push to a remote
  - Create a fork (GitHub)
  - Create a pull request (GitHub)

