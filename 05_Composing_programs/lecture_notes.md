# Review Answers

##What problems do operating systems solve?

1. **Hardware abstraction**:  interact with heterogeneous hardware through a common interface.
2. **Multitasking**:  Run several programs concurrently, managing their state independently.  Programs managed by operating systems are sometimes called _applications_ (hence the neologism _app_).

##What is a system shell?

A system shell is a command-line interface to the _operating system_, presented through a program called a _terminal emulator_ (usually shortened to _terminal_).

##What is an interpreter?

An interpreter is a program, managed by the OS, that translates human-readable _source code_ into executable _machine code_, and executes it.

##What is the `python` shell command?

The `python` command tells the OS to start the python interpreter, which is an application that is managed by the OS.  The python interpreter has two modes of operation.

It can launch an interactive shell:

    $ python

It can run a script non-interactively:

    $ python myscript.py

**Note:** The `$` symbol is a convention used to denote shell input.  It is *not* typed into the terminal.

#Review:  Our Tools

##1. What is `atom` ?

**Atom** is a _text editor_.  It edits text, and nothing else.

##2. What is `ipython` and why should it be preferred over `python`?

**IPython** is an interactive python shell.  It behaves similarly to the `python` command, but includes nice features for programmers including:

 - colorized tracebacks (we'll talk about those later)
 - `?` syntax for documentation
 - tab-completion
 - `%` syntax for "magic" commands (we'll talk about those later, too)

# Programming in Python

##Points to get across:

1. Programming languages impose a structure on your reasoning
2. Such approaches are called "programming paradigms"
3. Python's programming paradigm is OOP

##On OOP:

###Metaphorical level

1. Objects are the basic unit of python code
2. Objects are typed
3. Type tells you something about how you should use the object

###Practical level

1. Introduce duck-typing:  "What can my object do?"
    - Check the methods
    - Use the docs
1. Demonstrate function and caveats for each type.
1. Take Questions

#Control Structures

Straightforward.  Demonstrate and emphasize `=` vs `==`
