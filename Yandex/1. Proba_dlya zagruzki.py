import sys
 
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

a = list(map(int, input().split()))

data = input().split()
day, hour, min, rid = map(int, data[:4])
 
result = 0
for ch in s:
    if ch in j:
        result += 1
 
print(result)