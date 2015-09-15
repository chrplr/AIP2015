#! /usr/bin/env python
# Time-stamp: <2015-09-14 22:00 christophe@pallier.org>
# -*- encoding: utf-8 -*-

""" simple game where the computer asks the human to guess a number between 1 and 100 """

import random


def main():
    target = random.randint(1, 100)
    print("I am thinking about a number between 1 and 100")
    guess = raw_input("Your guess? ")
    while int(guess) != target:
        if int(guess) < target:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")
        guess = raw_input("Your guess? ")

    print("You win! The number was indeed " + str(target))

if __name__ == '__main__':
    main()
