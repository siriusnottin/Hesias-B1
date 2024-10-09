def chiffrer_cesar(text):
  text_chiffre = ''
  i = 0
  while i < len(text):
    text_chiffre += chr(ord(text[i])+3)
    i+=1
  return text_chiffre

def dechiffrer_cesar(text):
  text_dechiffre = ''
  i = 0
  while i < len(text):
    text_dechiffre += chr(ord(text[i])-3)
    i+=1
  return text_dechiffre

