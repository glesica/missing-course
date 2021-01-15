#!/usr/bin/env python3

from random import randint

def roll():
    n = randint(1, 6)
    print(f"You rolled a {n}")

for i in range(100):
    roll()

