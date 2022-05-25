def split_and_join(line):
    line = line.split()
    line = "-".join(line)
    return line

line = input("Enter the line\n")
result = split_and_join(line)
print(result)