s, h = [], []
for _ in range(int(input())):
    q = input().split()
    if q[0] == '1': s.append(q[1]); h.append(('1', None))
    if q[0] == '2': h.append(('2', s.pop()))
    if q[0] == '3':
        act, val = h.pop()
        s.pop() if act == '1' else s.append(val)
    if q[0] == '4': print(s[-1])