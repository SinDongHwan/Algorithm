s, n = input().strip().split(' ')
n = int(n)

if 1 > len(s) or 10 < len(s):
    print(f"String length Error : {len(s)}")

if 1 > n or 5 < n:
    print(f"n value Error : {n}")

print(s*n)