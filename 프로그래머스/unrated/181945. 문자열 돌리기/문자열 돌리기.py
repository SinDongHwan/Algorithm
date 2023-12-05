str1 = input()
if 1 > len(str1) or len(str1) > 10:
    print(f"str1 length Error : {str1}")
    
for ch in str1:
    print(ch)