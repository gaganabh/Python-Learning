def swap_case(s):
  words = list(s)
  for word in words:
    if word.isalpha():
      if word.islower():
        print(word.upper(), end="")
      elif word.isupper():
        print(word.lower(), end="")
    else:
      print(word, end="")


if __name__ == '__main__':
  s = input()
  result = swap_case(s)
  print(result)