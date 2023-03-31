# Z-функция ("зет-функция") от строки — это массив длины n, i-ый элемент которого равен наибольшему числу символов, 
# начиная с позиции i, совпадающих с первыми символами строки s.

# Иными словами, z[i] — это наибольший общий префикс строки s и её i-го суффикса.
def z_func(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z

print(z_func('aaabaab'))