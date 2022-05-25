myfile = open("ip_address.txt", "r")
mylist = myfile.readline()
mylist = mylist.split('\n', 1)[0]
print(mylist)