% Composing Programs
% louist87@gmail.com
% Sep. 2015

# Review:  Core Concepts

##What problems do operating systems solve?

#ifdef ANSWERS
1. **Hardware abstraction**:  interact with heterogeneous hardware through a common interface.
2. **Multitasking**:  Run several programs concurrently, managing their state independently.  Programs managed by operating systems are sometimes called _applications_ (hence the neologism _app_).
#endif

##What is a system shell?

#ifdef ANSWERS
A system shell is a command-line interface to the _operating system_, presented through a program called a _terminal emulator_ (usually shortened to _terminal_).
#endif

##What is an interpreter?

#ifdef ANSWERS
An interpreter is a program, managed by the OS, that translates human-readable _source code_ into executable _machine code_, and executes it.
#endif

##What is the `python` shell command?

#ifdef ANSWERS
The `python` command tells the OS to start the python interpreter, which is an application that is managed by the OS.  The python interpreter has two modes of operation.

It can launch an interactive shell:

    $ python

It can run a script non-interactively:

    $ python myscript.py

**Note:** The `$` symbol is a convention used to denote shell input.  It is *not* typed into the terminal.
#endif

#Review:  Our Tools

##1. What is `atom` ?

#ifdef ANSWERS
**Atom** is a _text editor_.  It edits text, and nothing else.
#endif

##2. What is `ipython` and why should it be preferred over `python`?

#ifdef ANSWERS
**IPython** is an interactive python shell.  It behaves similarly to the `python` command, but includes nice features for programmers including:

 - colorized tracebacks (we'll talk about those later)
 - `?` syntax for documentation
 - tab-completion
 - `%` syntax for "magic" commands (we'll talk about those later, too)
#endif

# Programming in Python

##Programming languages are written for humans!

- All languages are compiled to machine code
- Programming languages are a tool for **structuring thought**

**x86 assembly** wants you to think in terms of CPU registers

    section .data
    str:     db 'Hello world!', 0Ah
    str_len: equ $ - str

    section .text
    global _start

    _start:
    mov	eax, 4
    mov	ebx, 1

    mov	ecx, str
    mov	edx, str_len
    int	80h

    mov	eax, 1
    mov	ebx, 0
    int	80h

**Brainfuck** wants you to think in terms of memory addresses and pointers:

    ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.

**Python** wants you to think in terms of physical _objects_:

    print "Hello world!"

# Object-Oriented Programming

1. OOP is a _programming paradigm_:  a way to think about your problem and your code.
1. OOP uses the metaphor of _objects_ to describe elements of code and their behaviors.

>In Python, _everything_ is an object!

## So, what is an object?

Two levels of analysis:

1. Metaphorical level:  what does the term _object_ tell me about how I should think about my problem?
1. Practical level:  what can I do with this thing called _object_, and where can I get one?

# Metaphorical level

##All data are not equal.  Python is a _strongly typed_ language:

- Data come in various forms, called _types_.
- Similar types behave similarly.  Different types behave differently.
- It makes sense to do certain things with certain data types, but not with others.

Adding integers:

    1 + 1

Dividing floats:

    38.7 / 3.2

Adding strings:

    "Hello " + "world!"

Adding an integer to a string:

    "I am " + 28 + " years old"

##Conclusions:

1. An object's type tells you something about how you're expected to use it.
1. **Know what you're manipulating at all times!**

# Practical level

##Common Object Types

| Type Name     | Python object | Use case | Caveats |
| ------------- |:-------------:| -------- | ------- |
| Boolean       | `bool`        | Representing truth | |
| Integer       | `int`         | Representing whole numbers | Beware of integer division!  Try `10 / 2` |
| Float         | `float`       | Representing decimal fractions | Beware of floating-point errors!  Try `.1 * 3` |
| String        | `str`         | Representing text | Beware of accents and diacriticals! |
| List          | `list`        | Maintaining an ordered sequence of objects that may change.  Useful for _homogenous_ types | |
| Tuple         | `tuple`       | Maintainging an immutable ordered sequence Useful for _heterogeneous_ types.| |
| Dictionary    | `dict`        | Associating one object (the _key_) to another (the _value_) | Dicts are _unordered_ |
| Set           | `set`         | Keeping track of values that were encountered.  Testing for the presence of multiple values. | Sets are unordered and contain at most one of each item.|

#Control Structures

Computers build upon automata by allowing for _data-dependent computation_.
How do we change the behavior of a program based on the value of a variable?

    x = 10
    if x > 10:
        print("Greater than 10")
    elif x:
        print("Less than 10, but nonzero")
    else:
        print("exactly 0")

`if` and `elif` evaluate the _expression_ that follows them.  If the statement evaluates to `True`, the block of code is executed.

All objects have a Boolean truth value:

    bool(0)
    bool(1)
    bool("")
    bool("false")
    bool([])
    bool([1, 2, 3])

Zero and null values evaluate to `False`.  Everything else evaluates to `True`.

#Comparison operators:

| Symbol | Meaning | Example |
| :----: | ------- | :-----: |
| `<`    | *Less than* | `1 < 4` |
| `>`    | *Greater than* | `2.3 > 0` |
| `==`   | *Equal to* | `1 == True` |
| `!=`   | *Not equal to* | `True != False` |

###WARNING:

- `=` is for assignment, i.e.:  `n_subjects = 20`
- `==` is for boolean evaluation, i.e.:  `{} == False`

This will throw an error:

    x = "hello"
    if x = "hello":
        print("success!")

#Exercises

1.  Write a script to test if two strings are equal.  If they are equal, print the string, otherwise print a message indicating that they are not equal.  Bonus:  edit your script to print the string in all capital letters.  (Hint:  look at the methods for `str` objects!)

2.  Write a script to test if a dictionary contains the key "x".  The expression `"x" in d` (where `d` is a dictionary) will evaluate to `True` if `"x"` is a key in the dictionary.  If the key is present, print its associated value.  If it is absent, do the same for the key `"y"`.  If niether key is present, print a message explaining the dictionary is empty.

#Functions

Functions are the basic element of abstraction in most programming languages.  They are used to:

- Prevent duplication of code
- Improve readability of code
- Prevent bugs

Functions take in objects, and _return_ objects.  Using a function is referred to as _calling_.  Function calls are denoted by parentheses, e.g.:

    sum([1, 3, 6, 2])

Functions are defined via the `def` keyword:

    def sum(terms):
        """Add all elements of a list together and return the result"""
        s = 0
        for i in terms:
            s += i

        return i

#Exercises

1. Create a function that takes three arguments `a`, `b`, and `c` that correspond to the three sides of a right triangle with `c` being the hypotenuse.  The function should calculate the length of the side for which `None` was passed using the Pythagorean theorem.  For example:  `calculate_missing_side(3, 8, None)` should return `8.544...`

2. Create a function called `map2` that takes a function as it's first argument and a list of integers as it's second argument.  `map2` should call the function passed into it once for each argument in the list and return a list containing all the results.   Next, write a function called `double` that doubles a number.  Call `map2` as follows:  `map2(double, range(10))`.
