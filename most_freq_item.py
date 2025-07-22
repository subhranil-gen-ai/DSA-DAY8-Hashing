def most_freq_item(s):
  freq={}
  for char in s:
    freq[char]=freq.get(char,0)+1
  most_count=max(freq.values())
  for key in freq:
    if freq[key]==most_count:
      return key,most_count
s='aabbbbccc'
print(most_freq_item(s))
