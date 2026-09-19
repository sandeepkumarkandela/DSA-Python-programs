n = int(input())
s = [("", 0, 0)]
res = []
while s:
    curr, o, c = s.pop()
    if len(curr) == 2 * n: res.append(curr)
    else:
        if o > c: s.append((curr + ')', o, c + 1))
        if o < n: s.append((curr + '(', o + 1, c))
for r in res:
    print(r)