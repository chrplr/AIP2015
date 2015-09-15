# Intermezzo

* Review together what has been learned so far, and compare with the lecture'objectives

* Clarify Python syntax

* Consolidate some practical skills and some notions of Python with simple exercices



# Objectives of the AIP


At the end, you should be able to write simple Python scripts to:

    - compute basic statistics from files containaing numeric data
    - compute the number of occurrences of words in a text file
    - play the "guess a number" game

Then, you should be able profit more from the other Ateliers (Atelier d'Experimentation Humaine, Atelier de Statistiques, ...)

. . .

Programming can be fun!

(we are doing some silly exercices, but this is like the first lessons with an instrument)

. . .

We have already covered most of the points (although superfically):

## Basic programming concepts

* instructions/sequential exectution
* forever loops
* conditional statements
* constants integers/floats/strings (insist that there are different types)
* variables
* lists/dictionaries
* loops over sequences
* functions/parameters/local variables
* modules
* file input/output
* string functions


## Practical skills


* Run a program from the command line
    - open a terminal, interact with the shell
    - navigate the directory structure with cd/ls
    - type commands, possibily with options or arguments
    - interrupt a running program (using the process manager)

* Execute a python script.
* Install missing modules
* Launch ipython and use it interactively (distinction shell/interpreter python)
* Use an editor (atom) to view/edit a Python script
* what to do when there is a crash/error message


**Exercice**

* Open a Terminal and run the python script `AIP2015/resources/python-scripts/human-guess-a-number.py`
* run `dualscope.py` in the same directory.
* open `human-guess-a-number.py` with the editor atom, change the maximum value from 100 to 1000, and rerun it.



# Python syntax

We have hardly mentioned Python's syntax yet (because it is boring...)

Let us go to the lecture 04_Python_in_a_nutshell

A peculiarity of Python: the use of indentation do delimit blocs of instructions.

Let us check the script  AIP2015/resources/python-scripts/human-guess-a-number.py and verify that it comprises only the elements just described.


# Exercices

## Expressions

(@) How much is worth 350 euros in USD if the exchange rate if 1.17 USD = 1 euro?


. . .

```python
350 * 1.17
```

You can use Python's command line as a calculator.

. . .



## Loops and conditional statements


(@) What does the following code do?

```python
if (2 + 2) == 5:
	print("Sorry?")
else:
	print("Bonjour!")
```

. . .

*Answer:* It prints 'Bonjour!'

. . .


(@) What does the following code do?

```python
while True:
	print('!')
```

. . .

*Answer:* It prints '!' forever. Press Ctrl-C to interrupt it. Or use the task manager of your operating system.


(@) What does the following program do?

```python
answer = ""
while answer != 'You are the best!':
	answer = raw_input('Who is the best?')
print('Sure!'
```

Run it!

. . .

(@) What does the following code do?

```python
for x in ('a', 'b', 'c', 'd', 'e'):
	print x=='c'
```

. . .

Run it!

Remark: strings are sequences, therefore the following code works in the same way:

```python
for x in 'abcde':
	print x=='c'
```


(@) How to print a string of 80 '#'?

. . .

```python
s = ""
for _ in range(80):
	s = s + "#"
print(s)
```

Remark: the operator '*' on strings can also be used "#" * 80

. . . 



(@) What does the following code do?

```python
reg0 = 10
reg1 = 5
while reg0 > 0:
	reg0 = reg0 - 1
	reg1 = reg1 + 1
print(reg0)
print(reg1)
```

. . .

Remember the register machine rodrego?


. . .

(@) How to improve the following program:

```python
print "2 * 1 = 2",
print "2 * 2 = 4"
print "2 * 3 = 6"
print "2 * 4 = 8"
...
print "2 * 10= 20"
```

. . .

```python
for i in range(1, 11):
	print "2 * " + str(i) + " = " + str(2*i)
```

. . .

(@) How to print all multiplication tables from 1 to 10?

```python
for a in range(1, 11):
	print('---')
	for b in range(1, 11):
		print str(a) + ' * ' + str(b) + ' = ' + str(a*b)
```


## Defining functions

(@) Try to guess what the following script does and run it:

```python
import turtle

def square(n):
  turtle.fd(n)
  turtle.right(90)
  turtle.fd(n)
  turtle.right(90)
  turtle.fd(n)
  turtle.right(90)
  turtle.fd(n)
  turtle.right(90)

square(50)
a = raw_input('stop?')
```

Define the following function and execute it

```python
def spirale():
    for n in (50, 60, 70, 80, 90, 100):
        square(n)
        turtle.left(30)
```

How would you improve this code?


(@) What does the following code do?

```python
nombres = []
while True:
        answer = raw_input('data point (Press just Enter to finish)?')
	if answer == '':
                break
	nombres.append(float(answer))

sum, sumsq = 0.0, 0.0
for x in nombres:
	sum = sum + x
	sumsq = sum + x*x

print(sum/len(nombres))
print(sumsq/len(nombres))
```


(@) define a function f that takes 'x' and 'y' as parameters and returns 0.5*(x+y/x).

. . .

```python
def f(x, y):
	return 0.5 * ( x + (y / x))
```

Compute f(10, 2), f(f(10,2),2), f(f(f(10,2),2),2), and so on.

Compute f(10, 9), f(f(10,9),9), f(f(f(10,9),9),9) and so on...

Compute f(10, 16), f(f(10,16),16), f(f(10,16),16,16),...

Computer f(10, 25), f(f(10,25),25), and so on...

Can you form a conjecture on what happens?



. . .



(@) write a script that plays computer-guess-a-number, that is, you think about a number and the computer makes a succession of guess, and you tell it whether it is too large, to low or correct.







