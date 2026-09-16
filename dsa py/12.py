st, m, ans = [], {')': '(', ']': '[', '}': '{'}, "YES"
for c in input().strip():
    if c in m.values(): st.append(c)
    elif not st or st.pop() != m[c]: ans = "NO"; break
print("NO" if st else ans)