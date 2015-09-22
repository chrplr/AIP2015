# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:11:54 2013

@author: pallier
"""

import string
 
def print_matching_line(filename, expr):
    print "#"*30
    print("Searching " + filename + " for " + expr + ":")
    for line in file(filename):
		if string.find(line, expr) != -1:
			print(line)

print_matching_line('alice.txt', 'Alice')
print_matching_line('alice.txt', 'Rabbit')
print_matching_line('alice.txt', 'rabbit')
print_matching_line('alice.txt', 'stone')
print_matching_line('alice.txt', 'office')
