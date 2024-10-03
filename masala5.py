ls = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd'] 
belgi = input("harf kiriting:\n")
ls1 = list(filter(lambda b: b.startswith(belgi), ls))
print(f"Ushbu listdagi elementlar {belgi} bilan boshlanadi: {ls1}")