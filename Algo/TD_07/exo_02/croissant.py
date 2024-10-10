def is_croissant(l):
  i = 0
  while i < len(l)-1:
    # print('Compare', l[i], 'with', l[i+1])
    if l[i] <= l[i+1]:
      i+=1
    else:
      return False
  return True
