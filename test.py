def convert(input):
  wordList=[]
  for char in input:
    currentWord=""
    if char==input[0] and wordList==[]:
      currentWord+=char.upper()     
    elif char.isupper():
      currentWord+=" "+char.lower()
    else:
      currentWord+=char
    wordList.append(currentWord)
    
  return ''.join(wordList).strip()

print(convert('PaulPhoenix'))