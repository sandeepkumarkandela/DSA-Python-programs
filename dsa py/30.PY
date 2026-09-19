s, curr_s, curr_num = [], "", 0
for c in input().strip():
    if c.isdigit(): curr_num = curr_num * 10 + int(c)
    elif c == '[': s.append((curr_s, curr_num)); curr_s, curr_num = "", 0
    elif c == ']': prev_s, num = s.pop(); curr_s = prev_s + num * curr_s
    else: curr_s += c
print(curr_s)