lst = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
rev_lst = [ele for ele in reversed(lst)]
counters = int(input("Number of counters: "))
lines = {}
for i in range(counters):
    lines[i] = []
count = 0
for i in rev_lst:
    if(count != counters):
        lines[count].append(i)
        count += 1
    else:
        count = 0
print(lines)