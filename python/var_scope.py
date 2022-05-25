## global Vars
calculate_to_units = 24 * 60 * 60
name_of_unit = "seconds"

def days_of_unit(num_of_days, custom_message):
  print(f"{num_of_days} daya has {num_of_days * calculate_to_units} {name_of_unit}")
  print(custom_message)

def scope_check(num_of_days):
  # local vars
  var_msg = "var inside the method"
  print(name_of_unit)
  print(num_of_days)
  print(var_msg)

days_of_unit(10, "hello")
print("All Good")
print("--------")

scope_check(20)
print("Awesome")


