% Reaction times
% christophe@pallier.org
% Sept. 2013

(@) Write a program, using pygame, that starts with an empty black screen and after one second, displays a small white dot at the center of the screen for 1 second, waits for another second and then quits (tip: use the function pygame.time.delay to wait for a given amount of time)

. . .

```python 
#include <simple-rt1.py>
```

. . .

- - -

(@) Start the following program, move the mouse into the pygame window and clik on it several times, press keys, ... close the window to quit.

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    print(pygame.event.event_name(event.type))

pygame.quit()
```

(you can skim through the tutorial at <http://lorenzod8n.wordpress.com/2007/05/30/pygame-tutorial-3-mouse-events/> )
to understand pygame's mouse events. Now, modify the previous code so that the dot remains on the screen until you press a mouse button.

. . .


```python
#include <simple-rt2.py>
```


. . .

- - -

(@) Look at the documentation of the function pygame.time.get_ticks() and add code to measure and print the reaction-times, that is the time between the onset of the dot's display and the mouse button press.

. . .


```python
#include <simple-rt2b.py>
```


. . .

- - -

(@) Modify the previous program to repeat the process for 32 trials, and:

* Make the time between the appearance of two dots a random duration between 1 and 2 secs (tip: use the function random.randint). 
* Record the reaction times in a list.
* At the end of the program, save the reaction times in a text file. 
* Run this program twice using your right hand and twice using your left hand, *trying to respond as fast as possible, but without making false alarms* (change the name of the text file to save into different text files). 

. . .


```python
#include <simple-rt3.py>
```


. . .

- - -

(@) Look at your reaction time data. If you know to do it, plot histograms with a spreadsheet program or R (or any other software)

Launch spyder. Go to the console window, in the options, set the working directory to the directory that contains reaction-times.csv. Type the following commands:

```python
f = open('reaction-times.csv')
l = []
for line in f:
	l.append(int(line))
l
plot(l)
hist(l)
mean(l)
median(l)
```

- - - 

(@) Back to the reaction time program, write a function that removes the 25% extreme data points in a list and returns the mean and standard errors of the remaining data points (not using numpy).


. . .


```python
#include <simple-rt4.py>
```


. . .

- - -

(@) Change the size of the dot so that it is 10 times bigger than previously. Rerun the experiment. How is your reaction times affected?  

(@) Now, change the contrast of the dot with the background (make it grey rather than white).  How is your reaction times affected?  

(@) Modify the previous program so that the color of target is randomly chosen between blue and red (with equal probability) at each trial. You still use only one response button.

(@) The task is to now to take a decision: one mouse button is assigned to blue and another one to red (if you only have one mouse button, use 2 keys and the KEYDOWN event). In the results file, save both the button pressed and the reaction times (on row per trial). Compare decision times to simple reaction times. 

(@) Modify the program so that the dot can appear (randomly) at one of two locations far on the left or far on the right of the center. How is your reaction time affected?

(@) (advanced): Modify the simple detection program so that the contrast can be modified at each trial. Write the program to find the threshold of detection of the do.


