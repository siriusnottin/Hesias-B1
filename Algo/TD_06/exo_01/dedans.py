def dedans(s,text):
  print('looking for', s, 'in', text)
  i = 0
  while i < len(text):
    if text[i] == s:
      return True
    i+=1
  return False
