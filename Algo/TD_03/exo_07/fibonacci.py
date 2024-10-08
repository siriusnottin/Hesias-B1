n = int(input('Entier : '))
f0 = 1
f1 = 1

if n == 1:
  print(f0, end='.\n')
elif n == 2:
  print(f0, f1, sep=', ', end='.\n')
else:
  print(f0, f1, sep=', ', end=', ')
  i = 3
  while i <= n:
    fn = f0 + f1
    print(fn, end=', ' if i < n else '.\n')
    f0, f1 = f1, fn
    i += 1
