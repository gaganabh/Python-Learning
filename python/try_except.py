calculate_to_units = 24 * 60 * 60
name_of_unit = "seconds"

def days_of_unit(num_of_days):
    return f"{num_of_days} day has {num_of_days * calculate_to_units} {name_of_unit}"

def validate_and_execute():
  try:
          val_in_int = int(val_var)
          if val_in_int > 0:
            final_val = days_of_unit(val_in_int)
            print(final_val)
          elif val_in_int == 0:
            print("you have entered zero, pls enter +ve number")
          else:
            print("you have entred -ve number")

  except ValueError:
          print("enter the valid number")

val_var = input("pls enter the value\n")

validate_and_execute()