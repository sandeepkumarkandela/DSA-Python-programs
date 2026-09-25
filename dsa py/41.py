q_arr, idx = [], 0
for _ in range(int(input())):
    c = input().split()
    if c[0] == '1': q_arr.append(c[1])
    if c[0] == '2': idx += 1
    if c[0] == '3': print(q_arr[idx])