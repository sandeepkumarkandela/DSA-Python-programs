s, f = [], False
for c in input().strip():
    if c == ')':
        op = False
        while s[-1] != '(': op |= s.pop() in "+-*/"
        s.pop()
        if not op: f = True; break
    else: s.append(c)
print("YES" if f else "NO")