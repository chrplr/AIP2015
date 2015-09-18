# Warm up

(@) What does the following code do?

```python
for i in (1, 2, 3, 4, 5):
	print("All work and no play makes Jack a dull boy")
```

. . .

Modify it to print the line 100 times (You want to do a loop, check python's documentation)

. . .

One possible solution, using a "while loop":

```python
n = 1
while n <= 100:
	print("All work and no play makes Jack a dull boy")
	n = n + 1
```

. . .

Another, using a "for loop" and the function `range`:

```python
for _ in range(100):
	print("All work and no play makes Jack a dull boy")
```

. . .

Modify the program to randomly select a name in the list (John, Jack, Paul, Tim) at each line.

(Hint: import the module "random")

. . .

```python
import random

NAMES = ('John', 'Jack', 'Paul', 'Tim')

for _ in range(100):
	name = random.choice(NAMES)
	print("All work and no play makes " + name +  " a dull boy")
```


-------------

(@) What does the following function compute?

```python
def mysterious(n):
	""" ???? """ 
	sum = 0
	for i in range(1, n+1):
		sum = sum + i
	return sum
```

. . .

It computes the sum of all integers between 1 and n.


Remark: Freidriech Gauss would probably have written:

```python
def sum2(n):
	""" returns the sum of integers between 1 and n """
	return n * (n + 1) / 2
```

