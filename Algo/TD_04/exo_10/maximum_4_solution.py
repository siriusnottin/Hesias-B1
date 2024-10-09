def maximum_2(x, y):
  if x > y:
    return x
  else:
    return y  

def maximum_4(a,b,c,d):
  return(maximum_2(maximum_2(a, b), maximum_2(c, d)))
