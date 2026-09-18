s = []
for t in input().split():
    if t not in "+-*/": 
        s.append(int(t))
    else:
        b, a = s.pop(), s.pop()
        if t == '+': s.append(a + b)
        if t == '-': s.append(a - b)
        if t == '*': s.append(a * b)
        if t == '/': s.append(int(a / b))
print(s[0])