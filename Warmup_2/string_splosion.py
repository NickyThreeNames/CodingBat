"""Given a non-empty string like "Code" return a string like "CCoCodCode". """

def string_splosion(str):
  result = ""
  for i in range(len(str)+1):
    result += str[:i]
  return result  
