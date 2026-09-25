d, h, t = {}, 0, 0
for _ in range(int(input())):
    q = input().split()
    if q[0] == '1': h -= 1; d[h] = q[1]
    if q[0] == '2': d[t] = q[1]; t += 1
    if q[0] == '3': print(d[h]); h += 1
    if q[0] == '4': t -= 1; print(d[t])
    if q[0] == '5': print(d[h])
    if q[0] == '6': print(d[t - 1])