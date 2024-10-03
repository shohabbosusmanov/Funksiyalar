a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
a = set(a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = set(b)
new = set()
new = list(a.symmetric_difference(b))


print(new)