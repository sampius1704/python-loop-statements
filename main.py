import turtle

sam_turtle = turtle.Turtle()
sam_turtle.speed(50)

def square():
  sam_turtle.forward(100)
  sam_turtle.right(90)
  sam_turtle.forward(100)
  sam_turtle.right(90)
  sam_turtle.forward(100)
  sam_turtle.right(90)
  sam_turtle.forward(100)
  
def triangle():
  sam_turtle.forward(100)
  sam_turtle.left(120)
  sam_turtle.forward(100)
  sam_turtle.left(120)
  sam_turtle.forward(100)

#elephant_weight = 500;
#ant_weight = 10;

#if elephant_weight<ant_weight:
 # {
 #   square()
 # }
#else:
 # sam_turtle.forward(100)


#count = 0
#while count<22:
 # count=count+1
  #print(count)

for count in range(4):
  triangle()
