def check_entered_value(num_of_elements):
   if num_of_elements.isdigit():
      print("Entered value is a number")
   else:
     print("Entred value is a string")

def check_entered_value_type():
  for num_of_elements in enter_list.split(","):
      check_entered_value(num_of_elements)

enter_list = input("please provide the random mix list using comma seprated \n")

check_entered_value_type()