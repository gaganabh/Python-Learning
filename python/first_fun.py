calculate_to_units = 24 * 60 * 60
name_of_unit = "seconds"

def days_of_unit(num_of_days):
  print(f"{num_of_days} daya has {num_of_days * calculate_to_units} {name_of_unit}")

days_of_unit(10)
days_of_unit(15)
days_of_unit(20)
print("All Good")