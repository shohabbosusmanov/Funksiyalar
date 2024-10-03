def fact(a):
    s = 1
    for i in range(1, a + 1):
        s *= i
    
    return s

n = int(input("n sonini kiriting:\n"))

print(fact(n))