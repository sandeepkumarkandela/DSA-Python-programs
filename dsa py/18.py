q, c = map(int, input().split())
s = []
for _ in range(q):
    p = input().split()
    if p[0] == '1':
        if not s or len(s[-1]) == c: s.append([p[1]])
        else: s[-1].append(p[1])
    if p[0] == '2':
        i = int(p[1])
        if 0 <= i < len(s) and s[i]:
            print(s[i].pop())
            if not s[i]: s.pop(i)
        else: print("EMPTY")