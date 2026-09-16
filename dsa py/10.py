s = []
for _ in range(int(input())):
    q = input().split()
    if q[0] == '1': s.append(q[1])
    if q[0] == '2': s.pop()
    if q[0] == '3': print(s[-1])
    if q[0] == '4': s.append(s[-1])