ages = [2, 5, 10, 13, 23, 30, 32, 40, 60, 70]
x = int(input("Random age: "))
min = ages[-1] - ages[0]
for i in ages:
    if(abs(i - x) < min):
        min = abs(i-x)
for i in ages:
    if(abs(i - x) == min):
        index = ages.index(i)
print(index)