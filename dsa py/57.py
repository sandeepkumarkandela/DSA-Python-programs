from collections import deque
q = deque()
for _ in range(int(input())):
    c = input().split()
    if c[0] == '1': q.append(int(c[1]))
    if c[0] == '2':
        t = int(c[1])
        while q and q[0] <= t - 300: q.popleft()
        print(len(q))