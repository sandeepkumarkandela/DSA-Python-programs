num, k = input().strip(), int(input())
s = []
for d in num:
    while k and s and s[-1] > d: s.pop(); k -= 1
    s.append(d)
res = "".join(s[:-k] if k else s).lstrip('0')
print(res if res else "0")