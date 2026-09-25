import sys
sys.setrecursionlimit(20000)
s = []
def push(x):
    if not s: s.append(x)
    else:
        t = s.pop(); push(x); s.append(t)
for _ in range(int(input())):
    q = input().split()
    if q[0] == '1': push(q[1])
    if q[0] == '2': print(s.pop())