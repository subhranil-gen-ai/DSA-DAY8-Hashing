def occurrence_each_char(s):
  freq={}
  for char in s:
    freq[char]=freq.get(char,0)+1
  return freq
s='aabbcccd'
print(occurrence_each_char(s))
