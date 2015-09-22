# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:58:03 2013

@author: pallier
"""
import random
letters = "abcdefghijklmnopqrstuvwxyz        "
text = "".join([ random.choice(letters) for i in range(1000000) ])
print(text)

dico = {}
for w in text.split():
	if not(dico.has_key(w)):
		dico[w] = 1
	else:
		dico[w] += 1
		
# affichage des fréquences en fonction de leur rang		
freqs = dico.values()

import numpy as np
import matplotlib.pyplot as plt

lf = np.sort(freqs)
lf = lf[::-1] # reverse

plt.plot(lf, 'ro')
plt.yscale('log')
plt.xscale('log')

plt.show()