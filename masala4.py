ls = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

ls1 = []

for i in ls:
    if i not in ls1:
        ls1.append(i)
        
print(ls1)