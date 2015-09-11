Introduction to Programming (AIP2015)
=====================================

## Instructors

- Christophe Pallier <christophe@pallier.org>
- Sylvain Charron <sylvain.charron@polytechnique.edu>
- Louis Thibault <louist87@gmail.com>

### Website:

The lectures materials are available in a git repositoty located at <https://github.com/chrplr/AIP2015>

To download them on your computer, follow [these instructions](./howtos/how-to-get-the-lectures-materials.html).

Too see the list of all html and pdf documents, check [index.html](index.html).

## Objectives

* Learn the principles of how computers work
* Learn the basic concepts of programming (instructions/variables/loops...)
* learn the bases of Python programming
* Learn how to execute, design, write and debug programs

(see below for more details about the contents of this series of lectures)

### Prerequisites:

This course is intended for beginners, but students who already have
rudiments in programming (e.g. only know Matlab) can benefit from it.
Also, note that knowledge of Python and of the skills listed below is
a requirement for the other hands-on classes (Ateliers) of the
Cogmaster.

Before attending AIP, it can help:
- to study the learning modules on 'Python' and 'the command line' at
(https://www.codecademy.com)[www.codecademy.com]
- have a peek at the documents in the 'resources' folder.

During or after AIP, you may be interested in
[MIT's Introduction to computer science and programming](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/) online course. 

Another excellent resource to go beyond this lecture is <https://mitpress.mit.edu/sicp/sicp.html>





More precisely, at the end of this series of lectures, you should have
acquired:

Basic programming concepts
--------------------------

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

For example, you should be able to write Python scripts to:
* search for items in a list
* find the largest number in a list of integers
* compute basic statistics from files containaint numeric data
* compute the number of occurrences of words in a text file
* play the "guess a number" game



Practical skills
----------------

You should know how to:

* Download some source code (e.g. Python) from the Internet (e.g. github) and display it.
* Run a program from the command line
    - open a terminal, interact with the shell
    - navigate the directory structure with cd/ls
    - type commands, possibily with options or arguments
    - interrupt a running program (using the process manager)

* Execute a python script.
* Install missing modules
* Launch ipython and use it interactively (distinction shell/interpreter python)
* Use an editor (atom) to view/edit a Python script
* Find/read Python's documentation
* what to do when there is a crash/error message

Computer's architecture
-----------------------

To program computers, it is necessary to have a rough idea of how they work.

* Computer = Automaton + Memory store (Turing machines)
* Intro to Machine language (Register machine Rodrego)
* High-level languages. Compilation/interpretation.
* What does an operating system do


Methodology of programming
--------------------------

* divide-and-conquer approach, piping
* writing code following our coding standards (see below)
* debug with 'print'



Remarks
-------

Our Coding standards:

* use a common template for all scripts
* force writing docstrings with aim, input & output descriptions
* avoid global variables except for constants (use uppercase for identifier)
* spaces around operators, after ',',...
* use explicit names (lowercase ascii)
* use comments sparingly, explain why, not how
* factoring code (each step is a function, put docstrings)
