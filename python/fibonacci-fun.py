# fibonacci function

def fibonacci(num):
    num1 = 1
    num2 = 1
    i = 0
    while i < num:
        print(num1)
        i = i + 1
        temp = num2
        num2 = num1 + num2
        num1 = temp


fibonacci(12)