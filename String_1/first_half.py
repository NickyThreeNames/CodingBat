"""Given a string of even length, return the first half. So the string "WooHoo" yields "Woo". """

def first_half(str):
  half = len(str)/2
  if len(str)%2==0:
    return str[:half]
