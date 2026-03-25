number = int(input("Enter a number: "))
count = 0
temp = number
if temp > 0:
    while temp > 0:
        temp //= 10
        count += 1
elif temp < 0:
    temp = -temp 
    while temp > 0:
        temp //= 10
        count += 1
else:
    count = 1
print("Total digits:", count)
