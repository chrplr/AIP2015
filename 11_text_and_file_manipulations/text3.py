# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:18:45 2013

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

# calcul des frequences des mots
dico = {}
for w in words:
	if not(dico.has_key(w)):
		dico[w] = 1
	else:
		dico[w] += 1

# affichage des frequences en fonction de leur rang		
freqs = dico.values()

import numpy as np
import matplotlib.pyplot as plt

lf = np.sort(freqs)
lf = lf[::-1] # reverse

plt.plot(lf, 'ro')
plt.yscale('log')
plt.xscale('log')

plt.show()


