% Python in a nutshell
% Christophe Pallier
%

# Using Python interactively

You can use Python in two ways:

1. **Interactively**, e.g. by launching `ipython` in a terminal, and typing python commands that are *interpreted* and *executed* when you press 'Enter'. 

* Open a terminal and start ipython
* Type the following lines 

    import turtle 
    turtle.circle(50)
    turtle;forward(100)
    turtle.circle(50)
	
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.heading()


. . .

This is ok if you quickly test an idea. But as soon as you quit ipython, you lose all traces of what you have done. To avoid that, you want to use the **Edit-run** approach

# Edit-run cycle

Using a **text editor**, e.g. *atom*, you write a program, that is, a series of commands ;

* start Atom
* Type the following lines

	import turtle
    turtle.circle(50)
	turtle.forward(50)
	turtle.left(120)
	turtle.forward(100)
	turtle.left(120)
	turtle.forward(100)
	turtle.left(120)
   	turtle.forward(50)


* save the buffer under the filename `myscript.py`
* *run* with a python interpreter, for example by typing `python myprogram.py` on a command line (or `%run myprogram.py` in ipython).


Remark:
* You can learn more about Turtle graphics by erading the documentation at <https://docs.python.org/2/library/turtle.html>
* there exist a third approach which combines interactivity and persistence --- the `ipython notebook`.

# First programs

### Warming up


Create a script `hello.py`, and run it:

	name = raw_input('What is your name?')
	print('Hello ' + name + '!')

Concepts: string constant, variable (name), affectation, string concatenation with '+'

. . .

	n = 10
	a = 'bonjour'
	o = [5.6, 7.8, 0.9]
	print(n)
	print(a)
	print(o)

	n = 15
	a = 'au revoir'
	o = ['toto', 'titi', 'tata']
	print(n)
	print(a)
	print(o)

Concept: variables and constants, affectation

. . .

	n = 10
	m = n
	n = n + 2
	print(m, n)

Concept: modifying a variable

. . .

	for x in [1, 2, 3, 4]:
		print(x*x + 2*x + 1)

Concept: loop

. . .

	numbers = [1, 2, 5, 10]
	y = [(x*x + 2*x + 1) for x in numbers]
	y

concept: lists (or sequences)

See <http://effbot.org/zone/python-list.htm>

. . .

	for _ in range(100):
		print('All work and no play makes Jack a dull boy')

Concepts: range to generate a list of numbers, 'for' loop, indentation of instuction block

. . .

	for name in ('Jack', 'John', 'Tim'):
		for _ in range(10):
			print('All work and no play makes ' + name + ' a dull boy!')

Concepts: list of strings, double imbrication

. . .



	first100 = range(1, 101)
	for n in first100:
		sum = sum + n
	print(sum)

. . .


	import random

	target = random.randint(1, 100)

	print("I am thinking about a number between 1 and 100")

	guess = raw_input("Your guess? ")

	while guess != target:
        if guess < target:
            print("Too low!")
        else:
            print("Tow high!")
        guess = raw_input("Your guess? ")

    print("You win! The number was indeed " + target)


Type this program in a text editor, save it as a python script (with extension .py) and run it.


Programs (a.k.a scripts)
========================

* A program typically consists in  a series of  *instructions* (aka *commands*).
* The main types of instructions are:
    - Function calls
    - Assignments to variables
    - Testing and branching instructions

Note that Python scripts also often contain sections of module importation and function definitions (to be explained later)

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
print(34)
myvar = 36
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

---------------------------




