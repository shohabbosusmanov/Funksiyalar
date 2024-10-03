ls = list(map(int, input("sonlarni probel bilan kiriting:\n").split()))
ls1 = [i for i in ls if ls.count(i) > 1]

print(ls1)