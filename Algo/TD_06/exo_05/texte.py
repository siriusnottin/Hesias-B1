import random

def texte():
  str = ''
  i = 1
  while i <= 50:
    rand_char = random.randint(ord('a'), ord('z'))
    str += chr(rand_char)
    i+=1
  print(str)

  min_letter = ord('z')
  min_index = -1
  j = len(str)-1
  while j >= 0:
    if ord(str[j]) <= min_letter:
      min_letter = ord(str[j])
      min_index = j
    j-=1
  print(chr(min_letter), min_index)

texte()
