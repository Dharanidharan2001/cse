##count and say
#eg:
#1
#11
#21
#1211
#111221

def countandsay(s):
    res=[]
    i = 0

    if s[i] == "-":
        print("input value should be in positive")
    else:
        while i<len(s):
            count = 1
            while i+1<len(s) and s[i] == s[i+1]:
                i+=1
                count+=1
            res.append(s[i]+str(count))
            i+=1
        if len(res)>len(s):
            return s
        else:
            return "".join(res)
s="a"
print(countandsay(s))

"""n=1 
for i in range(n):
    s=countandsay(s)
    print(s)"""