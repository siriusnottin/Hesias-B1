def reverse_str(str):
  str_reversed = ''
  i = len(str)-1
  while i >= 0:
    str_reversed += str[i]
    i-=1
  return str_reversed
