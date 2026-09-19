s = []
for p in input().strip().split('/'):
    if p == '..':
        if s: s.pop()
    elif p and p != '.':
        s.append(p)
print("/" + "/".join(s))