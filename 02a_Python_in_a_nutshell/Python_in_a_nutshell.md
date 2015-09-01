% Python in a nutshell
% Christophe Pallier
%


Remember, that you can use Python in two ways:

1. **Interactively**, e.g. by launching `ipython` in a terminal, and typing python commands that are *interpreted* and *executed* when you press 'Enter'. 

This is good if you quickly test an idea. But as soon as you quit ipython, you lose all traces of what you have done. To avoid that, you want to use the second approach:

. . .

2. Using an **Edit-Run** cycle: using a *text editor*, you write a program, that is, a series of commands ; then you save it, say with the filename `myscript.py, and you *run* with a python interpreter, for example by typing `python myprogram.py` on a command line.

. . .

3. Although a very nice third approach which combines interactivity and persistence --- the `ipython notebook` --- exists, we believe that students must first learn the second approach (Edit-Run).


Programs (a.k.a scripts)
========================

* A program typically consists in  a series of  *instructions* (aka *commands*).
* The main types of instructions are:
    - Function calls
    - Assignments to variables
    - Testing and branching instructions

Note that Python scripts also often contain sections of module importation and function definitions

-----------------

## function calls

```python
from math import sin, pi
print(sin(pi/2))
```

```python
from turtle import circle, forward
circle(50)
forward(100)
circle(50)
```

The arguments of functions can be constants, variables, other function calls.

```python
myvar = 34
print(34)
print(myvar)
print(math.sin(myvar))
```


-----------------------

### Assignments

```python
a = 24
b = 'bonjour'
c = ['aga', 'bobo', 'glop']
```

* variables are names that point to objects in memory

```python
a = 3 
b = a
print a, b
a = 4 # a points to a new object
print a, b
```

```python
a = [1, 2, 3] 
b = a    # points to the same object (a list)
c = a[:] # makes a copy
a[0] = 10
print a, b, c
```




----------------------

### Testing and branching

```python
response = 'no'
if response == 'ok':
   	print 'accepted'
else:
	print 'rejected'
```

```python
n = 0
while n < 10:
      n = n + 1
print n
```


---------------------------

Objects
-------

* Useful programs typically manipulates objects, e.g. to extract some information, transform it and modify the world.

