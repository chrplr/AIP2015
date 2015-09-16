Plan du cours :

- open then close a window in which stimuli will appear
- draw something in that window
- draw basic shapes
- modify the position of a stimulus
- modify the color of a stimulus
- control the timing

If we have time

- show an image in the window
- show some texte in the window

# Open and close a window

1. Open a terminal and launch an ipython interpreter
2. type the following command to get access to the pygame module and all its amazing possibilities
```
import pygame
```

3. Then you have to initialize all the things that pygame requires
```
pygame.init()
```

4. Nothing shows up yet, and that's normal. In order to be able to draw something you have to define a display window, which requires us to specify the width and height of the window
```
pygame.display.set_mode((400,300))
```

5. Now you can close your window
```
pygame.quit()
```

6. You might notice that there is still some pygame stuff running, so to actually close everything, quit the interpreter
```
quit
```

## Exercise
1. Try again, but this time, Use a variable to store the display window object
```
MY_WINDOW=pygame.display.set_mode((400,300))
```

2. Take a look at the variable attributes and methods using
```
MY_WINDOW. and hit the tabulation key
```

# Basic Pygame program

1. From the template Louis presented, make a little program with the commandes you just typed in the ipython interpreter
2. Save that program with an appropriate name
3. run it using the command line
```
python name_of_your_program.py
```

## Exercise
1. What do you notice?
2. Open a ipython interpreter to get access to the nice built-in help
3. Try to understand what does the `pygame.time.wait` function and use it in your program
4. Now, modify your program to display a window with different dimensions
5. Let's take a look together at the program prems.py

# Change the background color of the window

Now we will interact a little bit with that display window.

## Color code

The colors are coded using a triplet of values for its RED, GREEN and BLUE components.  
Each component intensity is represented by a number that can take values between 0 and 255 (it is coded on one 8-bit byte).  
Thus:

- RED is coded as `(255,0,0)`  
- GREEN is coded as `(0,255,0)`
- BLUE is coded as `(0,0,255)`
- BLACK is coded as `(0,0,0)`
- WHITE is coded as `(255,255,255)`

## A little explanation on display asynchrony

In order to control the timing of a stimulus appearance on a screen, drawing and displaying are two diferent steps.

1. you prepare a stimumus in the graphic memory of the video card of your computer using pygame functions
2. you tell the computer to show on the screen what you prepared with the `pygame.display.flip()` function

## Exercice

1. make a nex program from `prems.py`
2. use the `MY_WINDOW.fill()` method to change the color of the window
3. use `pygame.display.flip()` to actually display it
