Crash course in programming, with Scratch
=========================================
by christophe@pallier.org

Prequisite
----------

Ideally, you should have ran the tutorial "Getting Started with Scratch". on
[scratch.mit.edu](http://scratch.mit.edu) (to be found under the
'Create'tab). 


First steps
-----------

### Program 001

In the 'motion' group, take the instruction 'turn 15 degrees' and drag it onto the 'Scripts' panel. 

![](img/scratch_001.png)

Double-Click repeatedly on the block 'turn 15 degrees', you should see the cat ('sprite 1') rotate.

In Scratch, when one double-clicks an instruction in the 'Scripts' panel, the computer **executes** it.

### Program 002

Drag the instruction 'move 10 steps' from the motion group, and add it to the bottom of the instruction 'turn 15 degrees'. Change the value '10' into '50'. 

![](img/scratch_002.png)

You have just created a **block** of instructions, also known as a **script**. 

* Double-Click on the block and see the sprite moving.
* Note that inside a block, instructions are exectuted *sequentially*, one after the other. **Can you prove it**?
* Experiment with changing the **argument** of the instruction 'move' (Tip: to clear the drawing area, move the instruction 'pen/clear' to the script window and execute it)  


### Program 003

Click on the 'pen' group, and add 'pen down' at the top of the block.

![](img/scratch_003.png)

Run it.

### Program 004

Construct the following scripts and play with them until you are sure to understand the behavior of the computer..

![](img/scratch_004.png)


### Concepts learned so far

* Instruction
* Argument of an instruction
* Block of instructions and sequential execution

Loops 
-----

Computers are good at doing tasks repeatedly (as they do not get tired).

Click on the "Control" group, and try to construct the following script:

![](img/scratch_repeat.png)

* Clicking on the 'green' flag will execute the block of instructions
* The  'Repeat' instruction, execute the inner block of instruction a number of times specified as an argument. This is called a **loop**
* Adjust the parameter of the Repeat instruction so that the sprite draw a full circle when you click once on the green flag.
* Replace the repeat instruction by 'forever'.

### Repeat a block until 

Modify the script as follows:


![](img/repeat_until.png)

Tip: the condition 'key space pressed?' is in the 'Sensing' group.

This illustrates a **repeat..until loop**: the inner block is executed until the **condition** is satisfied.



### Two sprites

Add a new sprite, and duplicate the script from sprite1. Click on the green flag. You should see the two sprites running in circles.

![](two_sprites)

# Prove that the scripts associated to the two sprites run in *parallel* (rather than sequentially).

Conditional execution
---------------------

Create a new scratch project, and change the costume of the sprite into a ball.

Then write and execute the following script.

![](condition_001.png)
  
You should see the ball bounce on the edges. 


Variables
---------

Using the group 'variable', we are going to create a **variable** 'a' and make it display continuously the x-coordinate of the ball.

![](condition_002.png)

The concept of **variable** is very important. You can think of it as a name for a object that can change (here the object is a number).

Now study the following script:

![](function_001.png)

The loop is executed 100 times. Each time, the value of the variable `a` is incremented by 1, and is used to compute new `x` and `y` coordinates where to sprite is instructed to moved to.




