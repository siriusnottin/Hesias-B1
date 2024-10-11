def frequence(s):
    d = {}
    for k in s:
      d[k] = 0

    for letter in s:
      d[letter] += 1
    return d
