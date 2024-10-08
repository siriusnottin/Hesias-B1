n = int(input('Entrez un nombre: '));

#affiche la table de multiplication par n
# 1 * n
# ...
# 10 * n

i = 1
while i <= 10:
  print(f'{i} * {n} = {i * n}')
  i = i + 1
