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


(@) What does the following program do (% is the modulo operator that returns the remainder of the integer division)

```python
n = 100
while n > 0:
	if n%7 == 0:
		print(n)
	n = n - 1
```


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


(@) What does the following function do?

```python
def un(l):
	u = []
	for x in l:
		if not(x in u):
			u.append(x)
	return u
```


