% Exercices in Python
% Christophe@pallier.org
% Sept. 2015

Reading exercices in Python
===========================

(@) What does the following code do?

```python
if 2 + 2 == 5:
	print("Sorry?")
else:
	print("Bonjour!")
```

#ifdef ANSWERS
*Answer:* It prints 'Bonjour!'
#endif


(@) What does the following program do?

```python
state = 1
for i in range(100):
        if state == 1: 
            print('A')
        if state == 2:
            print('B')
		if state == 3:
		    print('C')
		state = state + 1
		if state == 4:
			state = 1
```

#ifdef ANSWERS
*Answer:* It prints a sequence of alternating A, B and C         

#endif

(@) What does the following program do (% is the modulo operator that returns the remainder of the integer division)

```python
n = 100
while n > 0:
	if n%7 == 0:
		print(n)
	n = n - 1
```

#ifdef ANSWERS
*Answer:* It prints the numbers between 1 and 100 that are divisible by 7

A more efficient version would be:

```python
	[x for x in range(101) if x%7 == 0]
```
#endif

(@) What does the function ssn do in the following code?

```python
def ss(l):
	s = 0
	for x in l:
		s = s + x * x
	return s
	
def ssn(n):
	return ss(range(n+1))
```

#ifdef ANSWERS
*Answer:* It returns the sum of squares of the first 'n' integers
#endif

(@) What does the following function do?

```python
def un(l):
	u = []
	for x in l:
		if not(x in u):
			u.append(x)
	return u
```

#ifdef ANSWERS
*Answer:* It returns the set of elements in the list l
#endif

