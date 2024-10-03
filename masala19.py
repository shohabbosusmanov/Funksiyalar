ls = list(map(int, input("sonlarni probel bilan kiriting:\n").split()))

juft = list(filter(lambda c: c % 2 == 0, ls))
toq = list(filter(lambda c: c % 2 == 1, ls))

print(f"juft: {juft}    toq: {toq}")