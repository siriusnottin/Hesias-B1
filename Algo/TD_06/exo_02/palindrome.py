def is_palindrome(str):
  str_reversed = ''
  i = len(str)-1
  while i >= 0:
    str_reversed += str[i]
    i-=1
  if str == str_reversed:
    return True
  else:
    return False
