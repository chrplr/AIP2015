#! /usr/bin/env python
# Time-stamp: <2015-09-06 15:35 christophe@pallier.org>
# -*- encoding: utf-8 -*-

""" simple game where the computer asks the human to guess a number between 1 and 100 """

from random import randint


def main():
    target = randint(1, 100)
    print("I am thinking about a number between 1 and 100")
    guess = raw_input("Your guess? ")
    while guess != target:
        if guess < target:
            print("Too low!")
        else:
            print("Tow high!")
        guess = raw_input("Your guess? ")

    print("You win! The number was indeed " + target)
    return

if __name__ == '__main__':
    main()
