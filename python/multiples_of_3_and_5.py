# to find the multiple of a number
def mult(m,n):
    for i in range(n,(m*n)+1,n):
        print(i,end=' ')


m=5
n=3
print(mult(m,n))

#sum of the multiplels 3 and 5
def summultiple():
    a=sum([i for i in range(1,100) if i % 3 == 0 or i % 5 == 0])
    print(a)


print(summultiple())