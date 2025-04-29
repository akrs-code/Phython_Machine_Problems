try:
    num1 = int(input("Enter your First Number "))
    num2 = int(input("Enter your Second Number "))
    result = num1/num2
    print(result)
    

except ValueError as x:
    print(x)
    
except ZeroDivisionError:
    print("Error! This is undefined")

