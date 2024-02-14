# Problem Statement: We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return true if it is possible to make the goal by choosing from the given bricks.

def make_bricks(small, big, goal):
    
    big_needed = goal / 5
    goal -= min(big_needed, big) * 5
    if goal <= small:
      return True
    
    return False
    
