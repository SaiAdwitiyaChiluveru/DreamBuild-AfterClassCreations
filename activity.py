num = int(input("Enter the base number: "))
pwr = int(input("Enter the power: "))
result = 1
for i in range(pwr):
    result = result * num
print("Result is:", result)