def ikkilik(m):
    s = ""
    while m > 0:
        s += str(m % 2)
        m //= 2
    s = s[::-1]
    return int(s)

n = int(input("n sonini kiriting:\n"))

print(ikkilik(n))