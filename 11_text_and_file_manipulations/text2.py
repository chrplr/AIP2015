# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:45:43 2013

@author: pallier
"""


import string
def remove_punctuation(text):
	punct = string.punctuation + chr(10)
	l = " " * len(punct)
	return text.translate(string.maketrans(punct, l))

textori = file('alice.txt').read().lower()
text = remove_punctuation(textori)
words = text.split()
print(words)

n1, n2, n3 = 0, 0, 0
for w in words:
	if w == 'alice':
		n1 = n1 + 1
	if w == 'rabbit':
		n2 = n2 + 1
	if w == 'office':
		n3 = n3 + 1
print n1, n2, n3

dico = {}
for w in words:
	if not(dico.has_key(w)):
		dico[w] = 1
	else:
		dico[w] += 1
		
print(dico)

for w in sorted(dico, key=dico.get, reverse=True):
    print w, dico[w]
 