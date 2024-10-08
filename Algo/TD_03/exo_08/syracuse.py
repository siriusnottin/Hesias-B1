n = int(input('Entier : '))

if n%2 == 0:
  n /= 2
  print(n, end='.\n')
else:
  n = (n*3) + 1

i = 1
while i <= n:
  