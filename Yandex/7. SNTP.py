with open("Yandex/input.txt") as file:
# with open("input.txt") as file:
    h_start, m_start, s_start = map(int, file.readline().strip().split(":"))
    h_time, m_time, s_time = map(int, file.readline().strip().split(":"))
    h_fin, m_fin, s_fin = map(int, file.readline().strip().split(":"))

time_start = h_start*3600 + m_start*60 + s_start
time_time = h_time*3600 + m_time*60 + s_time
time_fin = h_fin*3600 + m_fin*60 + s_fin

if time_fin < time_start:
    dist = (86400 - time_start) + time_fin
else:
    dist = time_fin - time_start

time_time = time_time + dist/2
if time_time >= 86400:
    time_time = time_time - 86400

if time_time - int(time_time) >= 0.5:
    time_time = int(time_time) + 1
else:
    time_time = int(time_time)

res_h = int(time_time // 3600)
res_m = int((time_time - res_h*3600) // 60)
res_s = time_time - res_h*3600 - res_m*60


print(f'{res_h:02}:{res_m:02}:{res_s:02}')
