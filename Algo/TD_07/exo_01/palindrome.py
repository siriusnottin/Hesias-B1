def is_palindrome(str):
  reversed_str = []
  i = len(str)-1
  while i >= 0:
    reversed_str.append(str[i])
    i-=1
  return reversed_str == str
# print(is_palindrome([1,3,'s',3,2]))
