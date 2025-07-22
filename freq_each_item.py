def freq_each_item(arr):
  freq={}
  for i in arr:
    freq[i]=freq.get(i,0)+1
  return freq
arr=[1,2,2,1,3]
print(freq_each_item(arr))
