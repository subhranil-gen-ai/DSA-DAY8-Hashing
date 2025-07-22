def max_freq_item(arr):
  freq={}
  for i in arr:
    freq[i]=freq.get(i,0)+1
  most_freq_count=max(freq.values())
  for key in freq:
    if freq[key]==most_freq_count:  
      return key
arr=[1,2,2,1,3,2]
print(max_freq_item(arr))
