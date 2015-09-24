% Pygame events
% christophe@pallier.org
% sylvain charron


### Today's schedule
1. lecture
 + introduction to pygame timing
 + introduction to pygame events

2. practice
 + get a reaction time
 + building a stroop experiment

- - -

### Set up your working environment

1. Open atom, open two "Project Folders"
    + 12-reaction-times
    + AIP_brouillons
2. Open a first command-line interface and change directory to go to your testing folder "AIP_brouillons". There you will run your programs by typing `python my_program_name.py`
3. Open a second command-line interface, go to AIP_brouillons, and lauch the ipython interpreter. There you will try littles pieces of code and check the ipython help, so start with typing
```python
import sys
import pygame
```

- - -

### Looking at the computer's clock

1. In your ipython command line, try several time the command
    ```
    pygame.time.get_ticks()
    ```

2. How would you retrieve the delay between two consecutive call to the function `pygame.time.get_tics()`?

. . .

    1. store initial time in a variable  
        t0 = pygame.time.get_tics()

    2. get the difference between the current ime and the recorded initial time  
        delay = pygame.time.get_tics() - t0

. . .

- - -

### Using `pygame.time.get_tics()` in a program

1. What would this little program do?
    ```python
    import sys
    import pygame

    pygame.init()

    MY_WINDOW = pygame.display.set_mode((600,300))
    MY_WINDOW.fill((0,0,0))
    pygame.display.flip()
    t0 = pygame.time.get_ticks()

    while pygame.time.get_ticks() < t0 + 2000:
        print("delay : " + str(pygame.time.get_ticks() - t0))

    print("Total delay : " + str(pygame.time.get_ticks() - t0))
    pygame.quit()
    sys.exit()
    ```



2. Make a new program `pygame_timing_01.py` from the pygame template and modify it to use the `while` loop from 1. instead of `pygame.time.wait()`

3. Reminder on creating new files from teplate using atom:
    + from the project folder `12_reaction-times/programs`, select the file `pygame_template.py`
    + using the secondary click menu, copy it
    + use the secondary click menu on the project folder `AIP2015_Brouillons` to paste the file in your testing folder
    + on the `pygame_template.py` copy, use he secondary click menu rename it as `pygame_timing_01.py`

- - -

### Frame Rate for advanced programers
Check the file `AIP2015/12_reaction-times/programs/pygame_frame_rate.py`, and try to adjust the timing to flip at each refresh (this is very useful for subliminal stimulation).  
It could be very tricky to achieve...

- - -

### Introduction to events

Events are recordings of things that happen to the computer, including the user's actions through the input devices: keyboard and mouse/trackpad

Events have different types, you need to import pygame.locals to get access to those types and more, such as key names
```python
import pygame
from pygame.locals import *
```

Constants that define key names could be found [in the pygame.key documentation](https://www.pygame.org/docs/ref/key.html)

Play a bit with the file `AIP2015/12_reaction-times/programs/pygame_event01.py`

- - -

### More one events

Events are stored in a stack as time goes by.

Some useful functions from `pygame.event`

* wait for an event
```python
pygame.event.wait()
```

* clear the stack using
```python
pygame.event.clear()
```

* retrieve the stack as a list
```python
pygame.event.get()
```

* more on [The pygame documentation](https://www.pygame.org/docs/ref/event.html)


- - -

### Example

Play a bit with the file
