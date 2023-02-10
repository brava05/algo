import sys
 
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
 
result = 0
for ch in s:
    if ch in j:
        result += 1
 
print(result)