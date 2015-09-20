
The challenge was to make a program that shows this optical illusion :  
["motion induced blindness"](http://www.michaelbach.de/ot/mot-mib/)

A very good strategy to confront a challenge in conputer science is to split up said challange in several less challenging bits.

As you can see, in our case the stimulus is a composition of

- a rotating black background with a pattern made of blue crosses
- 3 static yellow dots, equidistant from the center
- a static central dot whose color is alternating between green and red


It's a good strategy to start by the easiest part, and then progress with increasing difficulty.
In our case, we would thus proceed in this order

1. the side dots, because we know how to draw static constant dots at given positions with `pygame.draw.circle`, so let's call them side circles now
2. the central dot, because it requires two steps :
  1. drawing a static dot, as for side dots
  2. make its color change
3. the rotating pattern

It's usually a good method to check if you can re-use something you already made, for example

- drawing a circle
- setting the background color of a surface
- we just saw the solution to get the rotating python logo well centered, so you can anticipate that we will use a very similar code to rotate cross-spangled background around the center of the window.

So, let's start.

First, we set up our working environment

1. Open atom, where you will edit your program
2. Open a first command-line interface and change directory to go to your testing folder (the one I told you to call "AIP_brouillons"), you will use it to run your programs
3. Open a second command-line interface, go to AIP_brouillons, and lauch the ipython interpreter, you will use it to try littles pieces of code and see the help related to python commands, so start with typing
```
import pygame
pygame.init()
WINDOW_DIMENSIONS = (400,300)
MY_WINDOW = pygame.display.set_mode(WINDOW_DIMENSIONS)
```


# 1. Side circles

## 1.1 List what you need in order to draw one circle

1. If you don't remember the syntax, go to you `ipython` command line and type `pygame.draw.circle?`
> Docstring:  
> circle(Surface, color, pos, radius, width=0) -> Rect  
> draw a circle around a point

2. So now you need to provide 4 arguments
 - a surface: your window
 - a color: a triplet of values between 0 and 255
 - a position: a couple of values, which are the horizontal and vertical position of the center of the circle relatively to the top-left corner of the surface (in number of pixels)
 - a radius: just a value (in number of pixels)

3. so you can start by defining some variables to store values that will stay constant for your program, so by convention, their names are upper case. The color and radius are the same for each side cicle, so let's define
```
SIDE_CIRCLES_COLOR = (255,255,0)
SIDE_CIRCLES_RADIUS = 5
```

4. Now you can draw one cicle at a given position, for example the center of the window. You can try in your ipython command line

```
BACKGROUND_COLOR = (0,0,0)
MY_WINDOW.fill(BACKGROUND_COLOR)
pygame.draw.circle(MY_WINDOW, SIDE_CIRCLES_COLOR, (200,150), SIDE_CIRCLES_RADIUS)
pygame.display.flip()
```
## 1.2 Draw four side circles

4. In order to make it easy to define the positions, we will use 4 side circles. Grab a piece of paper and figure out the couple of horizontal and vertical positions of each circle which will be 100 pixels appart from the center of the window, knowing that the window size is 400 by 300 pixels

5. For example
 - 100 pixels right from the center => (200+100,150)
 - 100 pixels left from the center => (200-100,150)  
 - 100 pixels over the center => (200,150-100)
 - 100 pixels under the center => (200,150+100)

6. You could draw the four side circles one by one, and it would be tedious, and this is typically why we have loops. Here we know exactly how many iteration we need, so we can use a `for` iteration structure.

7. Thus we need something to iterate on, typically a list, but it could be a dictionary, a tuple,...
```
SIDE_CIRCLES_CENTERS = [(300, 150), (200, 250), (100, 150), (200, 50)]
MY_WINDOW.fill(BACKGROUND_COLOR)
for center in SIDE_CIRCLES_CENTERS:
    pygame.draw.circle(MY_WINDOW, SIDE_CIRCLES_COLOR, center, SIDE_CIRCLES_RADIUS)
pygame.display.flip()
```

8. Test it in ipython to see the 4 side dots on the pygame-operated window


## 1.3 Insert the code to draw four side circles in a program

You can start with the minimally appropriate pygame program template... well, minimal regarding our safety and good practice recommendations.  
You will find this template in `AIP2015/09_More_fun_with_pygame/programs/pygame_template.py`  

1. Create a new file from the template, using atom
    1. Prepare atom
        - In atom, go to the menu `File`, then `Add Project Folder` and select your `AIP2015/09_More_fun_with_pygame/` local repository.
        - It should now appear in the left panel of the atom window, and you should be aple to navigate this directory, and see the files in the `programs` sub-directory.
        - Do the same with your `AIP2015_Brouillons` directory.
    2. Use atom Project Folder panel to copy-paste a file
        - From `09_More_fun_with_pygame/programs`, select the file `pygame_template.py`
        - Using the secondary click menu, copy it, then use the secondary click menu on `AIP2015_Brouillons` to paste the file in your AIP2015_brouillons folder, finally, always with the secondary click menu rename it as `side_dots.py`

2. Fill the program file with the snippets of code you already have tested in ipython
    0. change the docstring to describe what your program is doing
    1. nothing to change to the `import` session
    2. add the required constants
    3. add the loop to draw the four side circles

3. In the **ipython command line**, in order to avoid confusion (and possible computer problems) between multiple pygame-operated windows, execute
```
pygame.quit()
quit
```
then just launch the ipython interpreter again.

3. In your **normal command line interpreter (not the ipython one)**, execute
```
python side_circles.py
```
4. If needed, the file `challenge_01.py` in `09_More_fun_with_pygame/programs` should be very similar to your own side_circles.py

5. For more seasoned coders, have a look at the file `programsside_circles_deluxe.py` for drawing as many centered shapes as you like, using a dictionary for side dots constants and comprehension lists (cf [one of the best explanation of coprenhension lists](http://sametmax.com/python-love-les-listes-en-intention-partie/)).

# 2. Blinking central dot

Basically you draw a circle in the center of the window, and later you draw the same circle with a different color.

## 2.1 Draw a circle then another one with a different color

Back to the ipython command line (by the way, when you have to pase a bloc of code lines, just type `%paste` at the ipython command prompt)

0. Just do the usual to get access to a pygame_operated window

1. Define what you need to draw the circle, just as you did for in 1.1
```
#clear the window
MY_WINDOW.fill(BACKGROUND_COLOR)
pygame.display.flip()
# ok, now for the central dot
CENTRAL_CIRCLE_CENTER = (200,150)
CENTRAL_CIRCLE_RADIUS = 100
CENTRAL_CIRCLE_COLOR_1 = (0,255,0)
CENTRAL_CIRCLE_COLOR_2 = (255,0,0)
# draw the first circle
pygame.draw.circle(MY_WINDOW, CENTRAL_CIRCLE_COLOR_1, CENTRAL_CIRCLE_CENTER, CENTRAL_CIRCLE_RADIUS)
# show the first circle
pygame.display.flip()
# contemplate your work
pygame.time.wait(1000)
# draw the second circle, show and contemplate
pygame.draw.circle(MY_WINDOW, CENTRAL_CIRCLE_COLOR_2, CENTRAL_CIRCLE_CENTER, CENTRAL_CIRCLE_RADIUS)
pygame.display.flip()
pygame.time.wait(1000)
```

2. Well, you know, each time you write something twice, you'd better make a loop. So here the think we loop about is the colors so let's define a color list whose elements are the colors we want
```
CENTRAL_CIRCLE_COLORS = [(0,255,0),(255,0,0)]
```

3. Make a loop, let's say, to get a green then a red dot
```
#clear the window
MY_WINDOW.fill(BACKGROUND_COLOR)
pygame.display.flip()
# and now the loop
for color in CENTRAL_CIRCLE_COLORS:
    pygame.draw.circle(MY_WINDOW, color, CENTRAL_CIRCLE_CENTER, CENTRAL_CIRCLE_RADIUS)
    pygame.display.flip()
    pygame.time.wait(1000)
```

## 2.2 Draw an alternating circle

Well it's still not really alternating...  
So, do you remember what happens when you tried naively to multiply a list by an integer?
1. Try the following command
```
print CENTRAL_CIRCLE_COLORS
print CENTRAL_CIRCLE_COLORS * 4
```

2. With this trick you could do 4 alternations between green and red like this:
```
for color in CENTRAL_CIRCLE_COLORS * 4:
    print color
    pygame.draw.circle(MY_WINDOW, color, CENTRAL_CIRCLE_CENTER, CENTRAL_CIRCLE_RADIUS)
    pygame.display.flip()
    pygame.time.wait(1000)
```

3. Remark:  
This time you have to put the
```
pygame.display.flip()
pygame.time.wait(1000)
```
inside the loop otherwise you would just write red dots over green dots and so on in the memory where you prepare the stimuli and then only display the final state, i.e. a red dot.

## 2.3 Write down a program

1. Set up everything
Exactly as you did before, copy the template in `AIP_brouillons` and rename it `atlernating_dot.py`

2. Add your constants between the imports and then functions, and the loop in the main function

3. In the **ipython command line**, in order to avoid confusion (and possible computer problems) between multiple pygame-operated windows, execute
```
pygame.quit()
quit
```
then just launch the ipython interpreter again.

3. In your **normal command line interpreter (not the ipython one)**, execute
```
python alternating_dot.py
```

4. If needed, the file `challenge_02.py` in `09_More_fun_with_pygame/programs` should be very similar to your own alternating_dot.py




# 3. Rotating background

## 3.0. Preparation

1. First, let's split up this rotating crossed background in sub-units
the first decompositions isolates two sub-units
    1. building the crossed pattern
    2. rotating it

2. Since we already have the function to nicely rotate an image, let's think a minute...
  + What it is that we can rotate?
      + A surface!
      + So Let's build the background be a surface!
  + If the background is a surface, what method typical of surface would we use to insert a blue cross pattern into it?
      + `.blit` !
      + What is it that could be "blited" inside the background?
          + Another surface!
          + So let's make the blue cross a surface too!
  + How easy is it to `.blit` a surface at a given position?
      + Meh, kinda easy actually?
          + Indeed, so we only have to make surface bearing a blue cross and `.blit` at different positions
              + So we will not use the `.move` method?
                  + Nah, it's a possibility, but why `.blit` then extract rectangle then `.move` then '.blit' again when you can just `.blit'`?

3. So, to summarize
    2. build a surface for the background
    1. build a surface for one blue cross
    3. `.blit` the cross all over the background
    4. prepare the rotated background and `.blit` it at the center of the window

4. Let's go back to your ipython command line! You know what you have to do to get a pygame-operated window called MY_WINDOW, but this time, let's have its color be something else than black in order to better see where our black background is located
  ```
  WINDOW_SIZE = (400,300)
  WINDOW_COLOR = (127,127,127)
  ```

5. **For the one who are not to afraid of math**,  
let's define the size of the different sub-units
  + in your impython window, `import math`

  + If we want the rotated background to always fit in the window, it's maximal dimensions i.e. it's diagonal should be less than the smaller dimension of the window
  ```
  window_dim = [dim for dim in MY_WINDOW.get_size()]
  window_dim.sort()
  background_dim = int(math.floor(window_dim[0] / math.sqrt(2)))
  ```

  + and if we want a crossed pattern similar to [this one]() we need an odd number of crosses that is not too small, as you know since you were in elementary school `7 x 3 = 21`, so you would have 7 x 7 crosses on the background, each on a 30 pixel square and it would look nice.
  ```
  crosses_per_dim = 7
  cross_dim = background_dim / crosses_per_dim
  background_dim = cross_dim * crosses_per_dim
  print  background_dim
  print cross_dim
  ```
  Remark:  
  Here we uwe the pythonic behavior of integer division to get the actual background_dim

  + Thus finally you get  
     + background_dim = 210 pixels
     + cross_dim = 30 pixels



## 3.1. Prepare the background

1. Build a surface for the background
    + Check the syntaxe
      ```
      pygame.Surface?
      ```
      > Docstring:  
      > Surface((width, height), flags=0, depth=0, masks=None) -> Surface  
      > Surface((width, height), flags=0, Surface) -> Surface  
      > pygame object for representing images

    + Define the constants you need,
      ```
      BACKGROUND_SIZE = (210,210)
      ```
      Remark :  
      The background shape is a square, as for its size, for the moment, let's just make it fit in the wndow

    + Create your surface
      ```
      BACKGROUND = pygame.Surface(BACKGROUND_SIZE)
      ```

    + Paint it black
      ```
      BACKGROUND_COLOR = (0,0,0)
      BACKGROUND.fill(BACKGROUND_COLOR)
      ```

2. Build a surface for one blue cross
    + Define the constants you need for the 30 pixel square on which you are going to draw the blue cross
    ```
    CROSS_TILE_SIZE = (30,30)
    CROSS_TILE = pygame.Surface(CROSS_TILE_SIZE)
    ```

    + Paint it white for the moment so that we could see it on the black background
    ```
    CROSS_TILE_COLOR = (250,250,250)
    CROSS_TILE.fill(CROSS_TILE_COLOR)
    ```

    + Draw a blue cross on the cross tile
    ```
    CROSS_COLOR = (0,0,255)
    CROSS_RECTANGLES = [(8,14,14,2),(14,8,2,14)]
    for r in CROSS_RECTANGLES:
        pygame.draw.rect(CROSS_TILE,CROSS_COLOR,r)
    ```

3. `.blit` the cross all over the background

    1. First, let's `.blit` one cross surface on the bare background surface, and then to `.blit` the background on you pygame-operated window    

        + In order to check the `.blit` syntaxe, remember that it is a method of the surface inside which you want to put some other surface
        ```
        .blit?
        ```
        > Docstring:  
        > blit(source, dest, area=None, special_flags = 0) -> Rect  
        > draw one image onto another

        Remark:  **source** is the surface you want to insert (here: the cross) and **dest** is a tuple `(horizontal_position_of_the_top-left_corner,   vertical_position_of_the_top-left_corner)` or a rectangle   `(horizontal_position_of_the_top-left_corner,   vertical_position_of_the_top-left_corner, width, height)` that defines  the position at which you want the inserted surface (here: the cross) to    appear, relatively to the top-left corner of the surface in which you   want to blit (here: the bare background square)

        + So you need a position. For the moment, lets define some constants to `.blit` the cross on the bare background and then the crossed background on the window
        ```
        CROSS_TILE_POSITION = (0,0)
        BACKGROUND_POSITION = (50,0)
        ```

        + Now you can `.blit` one cross tile on the background, and the background  on the window, then display the result
        ```
        BACKGROUND.blit(CROSS_TILE, CROSS_TILE_POSITION)
        MY_WINDOW.blit(BACKGROUND, BACKGROUND_POSITION)
        pygame.display.flip()
        ```

    2. Now, the only thing to change in order to `.blit` several CROSS_TILE on the background is to find how to iterate

        + You need to iterate over the horizontal and vertical dimention, which you could easily do with 2 nested `for` loops and a carefuly specified `range`. if needed, use the ipython help
        ```
        range?
        ```

        + You need to iterate for as much CROSS_TILE you can fit in the BACKGROUND
        ```
        for horizontal_position in range(0, BACKGROUND.get_width(), CROSS_TILE.get_width()):
            for vertical_position in range(0, BACKGROUND.get_height(), CROSS_TILE.get_height()):
                BACKGROUND.blit(CROSS_TILE, (horizontal_position, vertical_position))
        ```

    3. Display hte result on the pygame-operated window

        ```
        MY_WINDOW.blit(BACKGROUND, BACKGROUND_POSITION)
        pygame.display.flip()
        ```

4. Prepare the rotated background and `.blit` it at the center of the window

    1. In order to use the rotation that we already built in `AIP2015/09_More_fun_with_pygame/programsrotating_python_logo_solution.py`, let's first make a nice program with the background we just built

        + Same as before : go to `AIP_brouillons` copy `AIP2015/09_More_fun_with_pygame/programspygame_template.py` there under the name `rotating_background.py`.

        + Since we are making a lot of surfaces, it's a good opportunity to make a function that combines generating and coloring the surface in one step
        ```
        def make_surface(surface_size,surface_color):
            the_surface = pygame.Surface(surface_size)
            the_surface.fill(surface_color)
            return the_surface
        ```

        + If you need, compare your script with `AIP2015/09_More_fun_with_pygame/programschallenge_03.py`

    2. Insert the pieces of `AIP2015/09_More_fun_with_pygame/programsrotating_python_logo_solution.py` that you need to have your background revolve around the center of the window

        + replace
        ```
        BACKGROUND_POSITION = centerize(BACKGROUND, MY_WINDOW)
        MY_WINDOW.blit(BACKGROUND, BACKGROUND_POSITION)
        ```

        by
        ```
        for degres in range(0,ANGLE_MAX,ANGLE_STEP):
            MY_ROTATED_IMAGE = pygame.transform.rotate(MY_IMAGE, degres)

            MY_ROTATED_IMAGE_POSITION = centerize(MY_ROTATED_IMAGE, MY_WINDOW)

            clean_the_window(MY_WINDOW, BACKGROUND_COLOR)

            MY_WINDOW.blit(MY_ROTATED_IMAGE, MY_ROTATED_IMAGE_POSITION)
            pygame.display.flip()
        ```

        + do the necessary adaptations
            + variable name translations
            + define the angles for the rotation

    3. Now you can see what I meant about everything being rectangles!

        + If not, compare your code with `AIP2015/09_More_fun_with_pygame/programschallenge_04.py`.

        + or maybe you already changed the colors of the cross tile and the background and the window. If not, you can set them all to black now.

# 4. Combine the rotating background, the side circles and the central dot in one program

## 1. Start from your `rotating_background.py` program and add the adequate pieces of your `side_circles.py` and `atlernating_dot.py`

## 2. Do adjustements and enjoy!

    If needed, check the program `AIP2015/09_More_fun_with_pygame/programschallenge_05.py`

___
The End!
