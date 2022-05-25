
def count_substring(string, sub_string):
  count = 0
  i = string.find(sub_string)
  #print(i)
  while i != -1:
    count += 1
    i = string.find(sub_string, i+1)
  return count


string = input("provide string\n").strip()
sub_string = input("provide sub_string\n").strip()
count = count_substring(string, sub_string)
print(count)