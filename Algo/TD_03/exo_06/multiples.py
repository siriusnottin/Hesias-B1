i = 1
while 1 <= i <= 50:
  if i % 3 == 0 or i % 5 == 0:
    print(i, end='')
    print(',', end='')
  i += 1
print('.')
