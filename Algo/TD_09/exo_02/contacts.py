def existe(d, nom):
  for k in d:
    while k != nom:
      return False
    return True

def ajouter(d, nom, tel):
  if not existe(d,nom):
    d[nom] = tel
  return d

def supprimer(d, nom):
  if existe(d, nom):
    del d[nom]

def chercher_nom(d, nom):
  if not existe(d, nom):
    return -1
  for k in d:
    return d[nom]

def chercher_num(d, tel):
  for k in d:
    if d[k] == tel:
      return k
  return None
