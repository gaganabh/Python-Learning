def write_table(table_num):
    table_val = 1
    while table_val < 11:
      print(f"{table_num} * {table_val} = {table_num * table_val}")
      table_val = table_val + 1

def validate_and_execute():
  try:
    table_num = str(table_num_val)
    if table_num == "exit":
      print("you are exit from the program")
    else:
        table_num = int(table_num_val)
        if table_num > 0:
          final_value = write_table(table_num)
          print(final_value)
        elif table_num  == 0:
          print("you have entered zero, pls enter +ve number")
        else:
          print("you have entred -ve number, pls enter the value greater then zero")
  except ValueError:
    print("pls dont enter the text, enter the valid number")

table_num_val = ""
while table_num_val != "exit":
  table_num_val = input("Enter the number for which you want to write table = ")
  validate_and_execute()
