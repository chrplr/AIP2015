

Overview

1. Afficher une image dans la fenêtre pygame
2. Déplacer cette image
3. Appliquer une transformation à cette image
4. Le principe des surfaces dans pygame
5. Afficher du texte, le déplacer, le transformer
6. Les bases du timing
7. Récupérer un appui sur une touche du clavier
8. Combiner tout ça !


# Display and image in a pygame window

If you are connected to the internet, go get some creative commons images, for example [the python logo from wikimedia](https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg)

### How to load an image
```
MY_IMAGE = pygame.image.load('path_to_the_image').convert()
```

## Exercices

1. Get to an ipython interpreter and prepare what is needed for pygame
2. Load the image
3. Check what is the type of your object MY_IMAGE
4. and look at its attributes and methods

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

1. Get the rectangle taht defines the position of the window
2. 
3.

```
MY_WINDOW.get_rect().center
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
MY_IMAGE_POSITION.move
```

## Exercices

1. Try it on the ipython command line
2. Use what you did in ipython to build a little program that laods and display an image
3. Using a loop and a test on the horizontal position of the image, make p program to display an image then move it horizontally and bounce on the borders of the window.

___
Break
___

# Blit a hand_made surface


# Display some text

font = pygame.font.Font(None, 36)
text_surface = font.render("Hello There", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.center = background.get_rect().center
background.blit(text, textpos)

# Timing

# Get user keyboard answers






https://www.pygame.org/docs/tut/newbieguide.html
