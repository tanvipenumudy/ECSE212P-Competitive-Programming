a = int(input("Left: "))
b = int(input("Right: "))
number = int(input("Enter the number of digits: "))
digits = []
count = 0
for j in range(number):
    digit = int(input("Enter the digit: "))
    digits.append(digit)
for i in range(a, b + 1):
        while(i > 0):
            check = i % 10
            i = i // 100
            if(check in digits):
                count += 1
print("The numbers are: " + str(count))