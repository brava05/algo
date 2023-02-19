def generate(current, open, closed, n, i):
    if len(current) == 2*n:
        print(i)
        print(current)
        return
    if open<n:
        print(i)
        print(current)
        generate(current+'(', open+1, closed, n, i+1)
    if open > closed:
        print(i)
        print(current)
        generate(current+')', open, closed+1, n, i+1)

generate("", 0, 0, 3, 0)

