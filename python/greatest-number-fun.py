# greatest number function

def greatest(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print(num1, " is the greatest number")
        else:
            print(num3, " is the greatest number")
    elif num2 > num3:
        print(num2, " is the greatest number")
    else:
        print(num3," is the greatest number")

a = 16
b = 12
c = 15

greatest(a,b,c)


# or the other way

def big(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    elif n2 > n3:
        return n2
    else:
        return n3

p = 9
q = 2
r = 34
print(big(p,q,r))
#print(B)