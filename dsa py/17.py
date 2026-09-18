q, c = map(int, input().split())
s = []
for _ in range(q):
    p = input().split()
    if p[0] == '1':
        if not s or len(s[-1]) == c: s.append([p[1]])
        else: s[-1].append(p[1])
    if p[0] == '2':
        print(s[-1].pop())
        if not s[-1]: s.pop()