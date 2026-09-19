res, num, sign, s = 0, 0, 1, []
for c in input().replace(" ", "") + '+':
    if c.isdigit(): num = num * 10 + int(c)
    elif c in "+-": res += sign * num; num, sign = 0, 1 if c == '+' else -1
    elif c == '(': s.extend([res, sign]); res, sign = 0, 1
    elif c == ')': res += sign * num; num, res = 0, res * s.pop() + s.pop()
print(res)