def all_variants(n, prefix, open, closed):
    if len(prefix) == 2*n:
        print(prefix)
        return
    if open < n:
        all_variants(n, prefix+"(", open+1, closed)
    if open > closed:
        all_variants(n, prefix+")", open, closed+1)


def main():
    n = int(input())
    all_variants(n, "", 0, 0)

if __name__ == '__main__':
    main()