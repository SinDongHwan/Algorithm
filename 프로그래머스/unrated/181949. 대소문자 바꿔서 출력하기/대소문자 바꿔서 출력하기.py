s = input()
if 1 > len(s) or len(s) > 20 :
    print(f"String Length Error : {len(s)}")

result = ""
for ch in s:
    if ch.islower():
        result += ch.upper()
    else:
        result += ch.lower()

print(result)