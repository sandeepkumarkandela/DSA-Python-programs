s1, s2 = [], []
for _ in range(int(input())):
    q = input().split()
    if q[0] == '1': s1.append(q[1])
    elif q[0] == '2':
        if not s2:
            while s1: s2.append(s1.pop())
        print(s2.pop())