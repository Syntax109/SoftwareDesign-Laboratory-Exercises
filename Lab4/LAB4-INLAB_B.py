def product(num1,num2):
    if num2 == 0:
        return 0
    else:
        return num1+product(num1,num2-1)
num1 = int(input("Enter first Integer: "))
num2 = int(input("Enter second Integer: "))
print("the product of" , num1 , "and" , num2 , "is:" , product(num1,num2))
