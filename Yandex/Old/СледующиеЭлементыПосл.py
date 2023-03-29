n = int(input())
indices = [int(i) for i in input().split()]
results = {i: i if i < 3 else None for i in indices}
k = max(indices)
a, b, c = 0, 1, 2
for i in range(3, k + 1):
    a, b, c = b, c, a + c
    if i in results:
        results[i] = c
print(" ".join(str(results[i]) for i in indices))