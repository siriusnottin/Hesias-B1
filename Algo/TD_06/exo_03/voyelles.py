def voyelles(str):
  i = 0
  str_voyelles = ''
  while i < len(str):
    if str[i] == 'a':
      str_voyelles += str[i]
    elif str[i] == 'e':
      str_voyelles += str[i]
    elif str[i] == 'i':
      str_voyelles += str[i]
    elif str[i] == 'o':
      str_voyelles += str[i]
    elif str[i] == 'u':
      str_voyelles += str[i]
    elif str[i] == 'y':
      str_voyelles += str[i]
    i+=1
  return str_voyelles
