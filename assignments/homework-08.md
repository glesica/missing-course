# Homework 8

Create a Dockerfile that defines a container that, when run, uses the
[cowsay](https://packages.ubuntu.com/focal/cowsay) application to print the
contents of an environment variable called `COWSAY_TEXT`.

Cowsay is easy to use. When it is run, it will print out any arguments passed to
it in a fun speech bubble above a cow. See below.

```
➜ cowsay I am a cow and I say things
 _____________________________
< I am a cow and I say things >
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

**Important Note:** In order to run `cowsay` in an Ubuntu container you need to
specify the full path to the executable, which is `/usr/games/cowsay`. This is
because `/usr/games` isn't in the `PATH` in the Ubuntu container image. This is
probably to simplify the image.

