# Требуется вычислить для неё префикс-функцию, т.е. массив чисел pi[0 ... n-1],
# где pi[i] определяется следующим образом: это такая наибольшая длина наибольшего собственного суффикса подстроки 
# s[0 ... i], совпадающего с её префиксом (собственный суффикс — значит не совпадающий со всей строкой). 
def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


def kmp(text,sub):
    len_sub = len(sub)
    new_text = sub+"#"+text
    pi = prefix(new_text)
    print(pi)
    res = []
    for i in range(len_sub+1, len(new_text)):
        if pi[i] == len_sub:
            res.append(i-2*len_sub)
    print(res)

# print(prefix('aaabcaaab'))
kmp('aaabcaaab', 'aaab')