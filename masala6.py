list1 = [1, 2, 3, 4, 5] 
list2 = [11, 22, 33]
list3 = []

mx = max(len(list1), len(list2))

for i in range(mx):
    if i < len(list1) :
        list3.append(list1[i])
    if i < len(list2) :
        list3.append(list2[i])
        
print(list3)