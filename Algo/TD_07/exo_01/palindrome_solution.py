def is_palindrome(l):
  i = 0
  while i < len(l)/2:
    if l[i] != l[-1-i]:
      return False
    i+=1
  return True
