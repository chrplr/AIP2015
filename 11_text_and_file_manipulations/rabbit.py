
# -*- encoding: utf-8 -*-

for a in file('alice.txt'):
  if ('Rabbit' in a) or ('rabbit' in a) or ('office' in a) or ('stone' in a):
      print(a)
