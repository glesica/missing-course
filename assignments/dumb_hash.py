#!/usr/bin/env python3

def dumb_hash(pw: str) -> str:
    h = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    for c in pw:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            h[i] += ord(c)
        elif c in "abcdefghijklmnopqrstuvwxyz":
            h[i] += ord(c) * 2
        else:
            h[i] += ord(c) * 4
        
        i = (i + 1) % len(h)

    digest = ""
    for v in h:
        digest += hex(0x1000 + v)[2:6]

    return digest


def _main():
    from sys import argv
    if len(argv) == 2:
        pw = argv[1]
        hashed_pw = dumb_hash(pw)
        print(hashed_pw)
    else:
        print("Usage: ./dumb_hash.py <PASSWORD>")


if __name__ == "__main__":
    _main()

