pr, st, res = {'+':1, '-':1, '*':2, '/':2, '^':3}, [], []
for c in input().strip():
    if c.isalnum(): res.append(c)
    elif c == '(': st.append(c)
    elif c == ')':
        while st[-1] != '(': res.append(st.pop())
        st.pop()
    else:
        while st and st[-1] != '(' and pr.get(c, 0) <= pr.get(st[-1], 0): res.append(st.pop())
        st.append(c)
while st: res.append(st.pop())
print("".join(res))