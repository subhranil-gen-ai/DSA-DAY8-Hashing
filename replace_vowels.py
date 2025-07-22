def replace_vowels(s):
  result = ""
  for char in s:
    if char.lower() in 'aeiou':
      result += "*"
    else:
      result += char
  return result
s='hello'
print(replace_vowels(s))
