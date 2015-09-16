import turtle

def square(n):
  turtle.fd(n)
  turtle.right(90)
  turtle.fd(n)
  turtle.right(90)
  turtle.fd(n)
  turtle.right(90)
  turtle.fd(n)
  turtle.right(90)

def spirale():
    for n in (50, 60, 70, 80, 90, 100):
        square(n)
        turtle.left(30)

spirale()
a = raw_input('stop?')
