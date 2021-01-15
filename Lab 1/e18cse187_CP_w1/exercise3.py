string = input("Enter the string:")
n = int(input("Enter the value of n:"))
lst = []
count = 1
for i in string:
    if(count == n):
        lst.append(i.upper())
        count = 1
    else:
        lst.append(i)
        count = count + 1
print(''.join(lst))