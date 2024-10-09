def maximum_3(x,y,z):
  # compare first two args
  max_nbr = 0
  if x > y:
    max_nbr = x
  else:
    max_nbr = y
  
  # compare last arg with the max of the 1st two args
  if z > max_nbr:
    return z
  else:
    return max_nbr
