def maximum_2(x, y):
  if x > y:
    return x
  else:
    return y  

def maximum_3(x,y,z):
  return maximum_2(maximum_2(x, y), z)

def maximum_4(n1,n2,n3,n4):
  return(maximum_2(maximum_3(n1,n2,n3),n4))
