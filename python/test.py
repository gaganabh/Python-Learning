def swap_case(s):
  x = ""
  for let in s:
    if let.isupper() == True:
       x+=(let.lower())
    else:
      x+=(let.upper())
  return x

if __name__ == '__main__':
  s = input("Provide the string to change the case \n")
  result = swap_case(s)
  print(result)