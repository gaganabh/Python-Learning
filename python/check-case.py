#declare the string

str =  '"this is a string"'
# check if string is in lower case
print('is',str,'in lower case:',str.islower())
# check if string is in upper case
print('is',str, 'in upper case:',str.isupper())
# change string to upper case
up = str.upper()
# check if string is in upper case
print('is',up,'in upper case:',up.isupper())
# check if string is in lower case
print('is',up,'in lower case:',up.islower())
# change string to title format
ttl = str.title()
print('is',ttl,'in title format:',ttl.istitle())
# check if string contains only alphabets
print('is',str,'contains only alphabets:',str.isalpha())
# check if contains numbers or alphabets
print('is',str,'contains numbers or alphabets:',str.isalnum())
# check if contains only digits
print('is',str,'contains only digits:',str.isdigit())