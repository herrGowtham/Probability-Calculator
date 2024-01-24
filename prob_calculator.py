import copy
import random
from collections import Counter

class Hat:

  given_contents = []

  def __init__(self,**kwargs):

    self.balls = kwargs
    self.given_contents.clear()

    for i in range(len(self.balls.values())):
      for j in range(list(self.balls.values())[i]):
        self.given_contents.append(list(self.balls.keys())[i])

    self.contents = copy.deepcopy(self.given_contents)

  def draw(self,num_balls_drawn):
    self.num_balls_drawn = min(num_balls_drawn,len(self.given_contents))
    self.drawn_balls = []

    if self.num_balls_drawn > len(self.contents):
      self.contents = copy.deepcopy(self.given_contents)
      
    for chance in range(self.num_balls_drawn):
      self.drawn_balls.append(random.choice(self.contents))
      self.contents.remove(self.drawn_balls[chance])
      
    return(self.drawn_balls)
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expected_contents = []
  
  for i in range(len(expected_balls.values())):
    for j in range(list(expected_balls.values())[i]):
      expected_contents.append(list(expected_balls.keys())[i])
  print(expected_contents)

  M = 0
  N = 0

  while num_experiments > N:

    drawn_balls = hat.draw(num_balls_drawn)

    if all(Counter(expected_contents)[i] <= Counter(drawn_balls)[i] for i in Counter(expected_contents)):
      M +=1

    N +=1

  return (M/N)