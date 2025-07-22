def check_unique(s):
  freq={}
  for char in s:
    freq[char]=freq.get(char,0)+1
  for char in s:
    if freq[char]>1:
      return False
  return True
s='abcdefgg'
print(check_unique(s))
