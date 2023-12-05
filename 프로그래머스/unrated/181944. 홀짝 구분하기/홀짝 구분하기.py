a = int(input())

if 1 > a or a > 1000:
    print(f"a value Error : {a}")
    
if a%2:
    print(f"{a} is odd")
else:
    print(f"{a} is even")