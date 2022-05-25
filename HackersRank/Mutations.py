def mutate_string(string, position, character):
  string = list(string)
  string[position] = character
  string = ''.join(string)
  return string

string = input("Provide random string\n")
position, character = input().split()
output = mutate_string(string, int(position), character)
print(output)