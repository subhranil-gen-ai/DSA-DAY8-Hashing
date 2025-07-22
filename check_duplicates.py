def check_duplicates(arr):
  freq={}
  for i in arr:
    freq[i]=freq.get(i,0)+1
  for i in arr:
    if freq[i]>1:
      return True
  return False

arr=[1,2,2,1,3]
print(check_duplicates(arr))
