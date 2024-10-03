def func(j, k, l):
    if j + k == l :
        return 1
    return 0

a, b, c = map(int, input("a, b, va c sonlarini kiriting:\n").split())

print(func(a, b, c))