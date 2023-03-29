from collections import Counter

n = int(input()) 
a = [int(i) for i in input().split()] 

counter = Counter(a)

result = a[0]
max_count = counter[result]
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count

print(result) 