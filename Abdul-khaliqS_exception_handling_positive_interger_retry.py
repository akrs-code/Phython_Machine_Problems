def set_num(num):

    if num < 0:
        raise ValueError("Number cannot be negative.")
    print(f"The number is {num}")
    
try:
    user_input = int(input("Enter a number "))
    set_num(user_input)

except:
    print("Number cannot be negative.")

