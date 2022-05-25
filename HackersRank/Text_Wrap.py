def string_wrap(string, max_width):
     result = ""
     for count in range(0, len(string), max_width):
          result += string[count:count + max_width] + "\n"
     return result

string, max_width = input("enter the string\n") , int(input("wrap size\n"))

output = string_wrap(string,max_width)
print(output)