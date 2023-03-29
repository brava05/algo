n = int(input())
sessions = []
for _ in range(n):
    x, y = map(int, input().split())
    sessions.append((x, y))

events = []
for start, end in sessions:
    events.append((start, 1))
    events.append((end, -1))
events.sort()

max_number = min_time = cur_number = 0
for cur_time, operation in events:
    cur_number = cur_number + operation
    if cur_number > max_number:
        max_number = cur_number
        min_time = cur_time

print(min_time)