from collections import deque
q1, q2 = deque(), deque()

for _ in range(int(input())):
    c = input().split()
    if c[0] == '1': q2.append(c[1]); q2.extend(q1); q1.clear(); q1, q2 = q2, q1
    if c[0] == '2': q1.popleft()
    if c[0] == '3': print(q1[0])