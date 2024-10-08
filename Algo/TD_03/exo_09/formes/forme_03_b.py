# with a single main loop

# rows display
i = 0
while i < 5:
  # symbol display
  j = 0
  while j < 5:
    if j < 5-i-1:
      print(' ', end='')
    else:
      print('*', end='')
    j+=1
  print()
  i+=1
