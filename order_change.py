def order_change(s):
  result=""
  for char in s:
   if 'a' <= char <= 'z':
    result+=chr(ord(char)-32)
  return result
s='hello'
print(order_change(s))
