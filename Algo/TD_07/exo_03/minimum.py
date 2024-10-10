def minimum(l):
  min_value = l[0]
  min_index = 0
  i = 1
  while i < len(l):
    if l[i] < min_value:
      min_value = l[i]
      min_index = i
    i+=1
  return (min_value, min_index)

