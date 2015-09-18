

Overview

1. Afficher une image dans la fenêtre pygame
2. Déplacer cette image
3. Appliquer une transformation à cette image
4. Le principe des surfaces dans pygame
5. Afficher du texte, le déplacer, le transformer


# Display and image in a pygame window

If you are connected to the internet, go get some creative commons images, for example [the python logo from wikimedia](https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg)

### How to load an image

```
MY_IMAGE = pygame.image.load('path_to_the_image').convert()
```

Remarks:

- you should always know where you are in your filesystem
- the path to a file is the
- if you are using windows, try using "/" instead of "\"

## Exercices

1. Get to an ipython interpreter and prepare what is needed for pygame
2. Load the image
3. Check what is the type of your object MY_IMAGE
4. and look at its attributes and methods


1. You have to redo the 3 following steps

  * `import pygame`
  * `pygame.init()`
  * `MY_WINDOW = pygame.display.set_mode((400,300))`

2. Remarks:

- you should always know where you are in your filesystem
- the path to a file is the
- if needed try using "/" instead of "\\"


### How to prepare the image and then display it on a pygame window

A new method for our pygame window : `MY_WINDOW.blit()`

```
MY_WINDOW.blit(MY_IMAGE,(0,0))
pygame.display.flip()
```

the `blit` method actually draws a surface onto another surface.

## Exercices

1. Display the image on your pygame window
2. Play around with the `blit` method input arguments

# Move an image

Remember what I told you about the importance of rectangles in pygame ?

## center an image the easy way

1. Get the rectangle that defines the position of the image
2. Get its center
3. Give it the value of the center of the window

```
MY_IMAGE_POSITION=MY_IMAGE.get_rect()

MY_IMAGE_POSITION.center=MY_WINDOW.get_rect().center

MY_WINDOW.blit(MY_IMAGE,MY_IMAGE_POSITION)
pygame.display.flip()
```

## Exercices

1. Try it on the ipython command line
2. Try other positions by exploring a bit `MY_IMAGE`

## Move an image around the super easy way

```
NEW_SURFACE = MY_IMAGE_POSITION.move(horizontal_position_increment,vertical_position_increment)
```

## Exercices

1. Try it on the ipython command line
2. Use what you did in ipython to build a little program that laods and display an image
3. Using a loop and a test on the horizontal position of the image, make p program to display an image then move it horizontally and bounce on the borders of the window.

4. If you want to try more complex modification of a surface, you have access to many other functions: do `pygame.transform. and tab`

5. For exmaple if you would like to rotate an image:

```
for degres in range(0,2000,1):
    MY_ROTATED_IMAGE=pygame.transform.rotate(MY_IMAGE,degres)
    MY_WINDOW.blit(MY_ROTATED_IMAGE,MY_IMAGE_POSITION)
    pygame.display.flip()
```

# Blit a hand_made surface

You can do the same to a surface you define with

```
MY_OWN_SURFACE = pygame.Surface(horizontal_dimention,vertical_dimension)
```

# Display some text

First you need to define the size fo the font, then you buid a surface.  
since the text is actually a surface, you can do the same thing with it as with an image.  
For example, to center your text :

```
font = pygame.font.Font(None, 36)
MY_TEXT = font.render("Almost the end!", 1, (10, 10, 10))
MY_TEXT_POSITION = MY_TEXT.get_rect()
MY_TEXT_POSITION.center = MY_WINDOW.get_rect().center
MY_WINDOW.blit(text, textpos)
pygame.dipslay.flip()
```

Beware of accents and non-anglo-saxon characters!
