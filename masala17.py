def unli(c):
    s = ord(c)
    if 96 < s < 101:
        if s == 97 :
            return "e"
        elif 101 - s == s - 97: 
            return "a", "e"
        elif 101 - s > s - 96:
            return "a"
        else :
            return "e"
    elif 101 < s < 105:
        if s == 101 :
            return "i"
        elif 105 - s == s - 101: 
            return "e", "i"
        elif 105 - s > s - 101:
            return "e"
        else :
            return "i"
    elif 105 < s < 111:
        if s == 105 :
            return "o"
        elif 111 - s == s - 105: 
            return "i", "o"
        elif 111 - s > s - 105:
            return "i"
        else :
            return "o"
    elif 111 < s < 117:
        if s == 111 :
            return "u"
        elif 117 - s == s - 111: 
            return "o", "u"
        elif 117 - s > s - 111:
            return "o"
        else :
            return "u"
    return "u"
    
n = input("harf kiriting:\n")

print(unli(n))