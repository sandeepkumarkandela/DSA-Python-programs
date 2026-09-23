s = [0]
for c in input().strip():
    if c == '(': s.append(0)
    else: s[-1] += max(2 * s.pop(), 1)
print(s[0])