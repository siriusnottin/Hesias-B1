# using two loops

# rows display
i = 0
while i < 5:
  # symbol display
  j = 0
  while j < 5 - i - 1:
    print(' ', end='')
    j+=1
  while j < 5:
    print('*', end='')
    j+=1
  print()
  i+=1
