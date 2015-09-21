% Text manipulations 
% Christophe@pallier.org
% Sept. 2013


# Strings

In Python, text can be stored in objects called *strings*.

String constants are enclosed between single quotes

    'Bonjour le monde!'

Or double quotes


    "Bonjour le monde !"

Or "triple" quotes for multi-lines strings

    """
    Bonjour le monde!

    Longtemps je me suis levé de bonne heure,
	Les sanglots longs des violons,
    ...
	"""

It is also possible to insert a 'line break' within a string with the character '\n' (line feed; ascii code=10).

    print("ligne 1\nligne 2")


A string is a **sequence** of characters.

	a = 'bonjour'
	print(a[0])
	print(a[1])
	print(a[2])
	print(a[2:4])
	print(len(a))
	
	for c in 'bonjour':
		print(c)


Operations on strings

	a = 'bonjour'
	b = 'hello'
	a + b
	a + ' ' + b

They have a type 'str'.

    >>> type('bonjour')
    <type 'str'>

To convert objects to string representations:

	str(10)
	a = dict((("a",1), ("b",2)))
	str(a)
	b = ["alpha", "beta", "gamma"]
	str(b)
    ", ".join(b)

Splitting a string at a delimiter:

    a = 'alain marie jean marc'
    a.split(" ")


The string module contains a set of functions to manipulate strings, e.g.:

	import string
	string.upper(a)
	string.lower('ENS')

## search/replace a substring within a string

	a = 'alain marie jean marc'
    a.find('alain')
    a.find('marie')
	a.find('ma')
	a.find('marc')
	a.find('o')
	
	a.replace('marie','claude')
	a



Read (see [https://docs.python.org/2/library/string.html](https://docs.python.org/2/library/string.html])) to learn about more string functions.

See also *regular expression* (module 're') for more complex pattern search.



format strings:

	"%d + %d is %d" % (4, 5, 9)
	"%s is %d years old" % ('Jacques', 45)
	"%03d" % 1

See doc for information on format strings



# Interactive input from the command line:

```python
name = raw_input('Comment vous appelez-vous ? ')

print "Bonjour " + name + '!'
```

# Reading a text file


* With Atom, create a text file containing two lines of arbitrary content (using only ascii characters), and save it under the filename `test.txt`
* Execute the following script (in the directory where `test.txt` is located)

```python
    f = file("text.txt")
  	f.read()
	f.close()
```

...


```python
    f = file("test.txt")
	content = f.read()
	content.split("\n")
	f.close()
```


# Writing to a text file:

```python
	f = file('test2.txt', 'w')
	f.write("Attention")
	f.write("Ceci est")
	f.write("un essai")
	f.close()
```

Important: to insert a  linebreak, you need to insert the character '\n'

Exercice: write the numbers 1 to 1000 (1 per line) in a file 'numbers.txt'.

. . .

```python
	f = file('numbers.txt', 'w')
	for i in range(1, 1001):
		f.write(str(i) + '\n')
	f.close()
```

```python
	f = file('numbers2.txt', 'w')
	for i in range(1, 1001):
		f.write("%d\n" % i)
	f.close()
```

```python
	f = file('numbers3.txt', 'w')
	for i in range(1, 1001):
		f.write("%04d\n" % i)
	f.close()
```


## the special case of csv files (comma separated values)


* Open a spreadsheet, e.g. with Excel or LibreOffice Calc.
* Create a small table with 3 colums and 4 lines:

-------   ----------  ----------
   cond            x           y
      a          2.0         4.2
	  a          3.0         5.4
	  b          4.0         3.1
	  b          5.0         3.9 
-------   ----------  ----------


* Use 'save as' to save the file with a *csv format*.
* Using a text editor, e.g. atom, open the file you have just saved.

Notice that a csv file is a *text file* (contrary to a .xlsx file, which uses a binary, proprietary format).

To store data, it is generally a good idea to use a text format rather
than a binary format.

Not only it is better for humans, but it makes it easier to import
other software, e.g. Python.




```python
import csv
f = file('aga.csv')
data = csv.reader(f, delimiter=',')
for row in data:
	print(row)
```

. . .

We could modify this program to compute the averages of each column.

But it would be tedious. Rather, we can use the module pandas:


```python
import pandas as pd

data = pd.read_csv('aga.csv')

data.x.mean()
data.y.mean()
data.groupby('cond').y.mean()
```

. . .

```
import matplotlib.pyplot as plt

plt.plot(data.x, data.y)
plt.show()

```



# Exercices

Download [Alice in Wonderland](http://www.pallier.org/cours/AIP2013/alice.txt).

(@) Write a program that prints all the lines that contain the string 'Alice'.

. . .

```python
import string
text = file('alice.txt')
for line in text:
	if string.find(line, 'Alice') != -1:
		print(line)
```

Modify your program to print the lines containing 'Rabbit', 'rabbit', 'stone', 'office'.

```python
import string
 
def print_matching_lines(filename, expr):
    print "#"*30
    print("Searching " + filename + " for " + expr + ":")
    for line in file(filename):
		if string.find(line, expr) != -1:
			print(line)

print_matching_lines('alice.txt', 'Alice')
print_matching_lines('alice.txt', 'Rabbit')
print_matching_lines('alice.txt', 'rabbit')
print_matching_lines('alice.txt', 'stone')
print_matching_lines('alice.txt', 'office')
```

Get <http://www.pallier.org/cours/AIP2013/text3.py>



- - - 

(@) Here is a program that converts the text file into a list of words, removing the punctuation marks and converting everything in lower case. Run it.

```python
import string
def remove_punctuation(text):
	punct = string.punctuation + chr(10)
	return text.translate(string.maketrans(punct, " " * len(punct)))

textori = file('alice.txt').read().lower()
text = remove_punctuation(textori)
words = text.split()
print(words)
```

Now write a script that counts the number of occurences of 'Alice', 'Rabbit' or 'office' in the list of words.

. . .

```python
n1, n2, n3 = 0, 0, 0
for w in words:
	if w == 'alice':
		n1 = n1 + 1
	if w == 'rabbit':
		n2 = n2 + 1
	if w == 'office':
		n3 = n3 + 1
print n1, n2, n3
```



- - -

(@) Use a dictonary to store the number of occurrences of each word in Alice in Wonderland (the keys are the words, and the values and the number of occurrences; if word= ['a', 'a', 'b']; dico={'a':2, 'b':1}). 

. . .

```
dico = {}
for w in words:
	if not(dico.has_key(w)):
		dico[w] = 1
	else:
		dico[w] += 1
		
print(dico)

# print sorted by word frequencies
for w in sorted(dico, key=dico.get, reverse=True):
	print w, dico[w]
```

Get <http://www.pallier.org/cours/AIP2013/text2.py>


- - -

(@) Use numpy and matplotlib to plot the word log(frequencies) as a function of the rank of words on the abscissae (the most frequence word being ranked #1)

You can skim through <http://matplotlib.org/users/pyplot_tutorial.html>.

. . .

```python
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
```

Get <http://www.pallier.org/cours/AIP2013/text3.py>



Remark: The product rank X frequency is roughly constant. This 'law' was discovered by Estoup and popularized by Zipf. See  <http://en.wikipedia.org/wiki/Zipf%27s_law>. 

(@) (advanced) Plot the relationship between word length and word frequency.

- - -


(@) Generate random text (each letter from a-z being equiprobable, and the spacecharacter being 8 times more probable) of 1 million characters. Compute the frequencies of each 'pseudowords' and plot the rank/frequency diagram.

. . .

```python
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
```

Get <http://www.pallier.org/cours/AIP2013/text4.py>

. . .

- - -

(@) (advanced) compute the table of transition frequencies between words in Alice and generate random text following this pattern.

- - -

(@) Read about the MU Puzzle (<http://en.wikipedia.org/wiki/MU_puzzle>). Write a program that generates sequences of strings based on the following production rules and the initial state 'MI'

1.    xI -> xIU
2.    Mx -> Mxx
3.    xIIIy -> xUy
4.    xUUy -> xy

(Tip: use the function string.replace)

. . .

```python
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

n = 0
while n<10:
    r = random.randint(1,4)
    if r==1:
        news = rule1(s)
    if r==2:
        news = rule2(s)
    if r==3:
        news = rule3(s)
    if r==4:
        news = rule4(s)
    if news != -1:
        print(str(n) + ': ('+ str(r) + '): ' + s + ' -> ' + news)
        s = news
        n = n + 1
```

Get <http://www.pallier.org/cours/AIP2013/text5.py>


One way to perform pattern matching is to use regular expressions <http://docs.python.org/2/howto/regex.html#regex-howto>.



# Additional exercices


(@) Monte-Carlo estimation of PI

By taking pairs of random numbers uniformly distributed between 0 and 1, and checking if there are within the disk of radius 1 centered on 0, that is, if x**2+y**2 < 1, estimate the number PI.


. . .

```python
import random

N = 10000
within = 0

for i in range(N):
	x, y = random.uniform(0,1), random.uniform(0,1)
	if (x**2 + y**2) < 1:
		within += 1

print 4.0*within/N
```

. . .

