# Python Program to Swap Two Numbers using Functions #

def swap_numbers(a,b):
    temp =a
    a=b
    b=temp

    print("Before Swaping Two Numbers:num1 ={0} and num2 ={1} ".format(a,b))

num1 = float (input("Please Enter the Number a:"))
num2 = float (input("Please Enter the Number b:"))

print("After  Swaping Two Numbers:num1 ={0} and num2 ={1} ".format(num1,num2))
swap_numbers(num1,num2)



