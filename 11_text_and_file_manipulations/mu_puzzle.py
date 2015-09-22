# -*- coding: utf-8 -*-
"""
the MU Puzzle (<http://en.wikipedia.org/wiki/MU_puzzle>).

Created on Tue Sep 17 22:29:03 2013

@author: pallier
"""


import string,random


def rule1(s):
    if s[-1] == 'I':
        return s + 'U'
    else:
        return -1


def rule2(s):
    if s[0] == 'M':
        return 'M' + s[1:] + s[1:]
    else:
        return -1


def rule3(s):
    if s.find('III') != -1:
        return s.replace('III', 'U')
    else:
        return -1
 

def rule4(s):
    if s.find('UU') != -1:
        return s.replace('UU', '')
    else:
        return -1


s = 'MI'

n = 1
while n <= 10:
    r = random.randint(1, 4)
    if r == 1:
        news = rule1(s)
    elif r == 2:
        news = rule2(s)
    elif r == 3:
        news = rule3(s)
    elif r == 4:
        news = rule4(s)

    if news != -1:
        print('step' + str(n) + ': (rule ' + str(r) + '): ' + s + ' -> ' + news)
        s = news
        n = n + 1
