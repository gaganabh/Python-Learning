calculate_to_units = 24 * 60 * 60
name_of_unit = "seconds"
print(type(name_of_unit))
print(type(calculate_to_units))


def days_of_unit(num_of_days):
  print(num_of_days > 0)
  type_check = num_of_days >= 0
  print(type(type_check))

  if num_of_days > 0:
    return f"{num_of_days} day has {num_of_days * calculate_to_units} {name_of_unit}"
  elif num_of_days == 0:
    return "you have entered zero, pls enter +ve number"
  else:
    return "you entered a -ve value, pls enter the correct value"

def validate_and_execute():
  if val_var.isdigit():
      final_val = days_of_unit(int(val_var))
      print("result= " + final_val)
  else:
      print("enter the valid number")

val_var = input("pls enter the value\n")
validate_and_execute()