n = int(input("Enter a number (N): "))
# sum_even = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_even = sum_even
    i+=1

print("The sum of all even numbers from 1 and",n,"is",sum_even)

#Abdul-khaliq R. Solaiman