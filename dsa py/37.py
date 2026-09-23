b, f = [], []
for _ in range(int(input())):
    q = input().split()
    if q[0] == '1': b.append(q[1]); f.clear()
    if q[0] == '2' and len(b) > 1: f.append(b.pop())
    if q[0] == '3' and f: b.append(f.pop())
    if q[0] in '23': print(b[-1])