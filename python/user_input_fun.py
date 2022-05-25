calculate_to_units = 24 * 60 * 60
name_of_unit = "seconds"


def days_of_unit(num_of_days):
  return f"{num_of_days} day has {num_of_days * calculate_to_units} {name_of_unit}"

val_var = input("pls enter the value\n")
int_val = int(val_var)

final_val = days_of_unit(int_val)
print(final_val)

