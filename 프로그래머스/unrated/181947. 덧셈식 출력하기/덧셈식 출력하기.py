a, b = map(int, input().strip().split(' '))
if 1 > a or a > 100:
    print(f"a value Error : {a}")
if 1 > b or b > 100:
    print(f"b value Error : {b}")
    
print(f"{a} + {b} = {a+b}")