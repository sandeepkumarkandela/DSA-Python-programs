n = int(input())
start = balance = deficit = 0
for i in range(n):
    p, d = map(int, input().split())
    balance += p - d
    if balance < 0:
        deficit += balance
        start = i + 1
        balance = 0
print(start if balance + deficit >= 0 else -1)