def make_bricks(small, big, goal):
    
    big_needed = goal / 5
    goal -= min(big_needed, big) * 5
    if goal <= small:
      return True
    
    return False
    
