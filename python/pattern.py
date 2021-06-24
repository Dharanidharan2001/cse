# right tiangle
n=3
for i in range(0,n):
    for j in range(0,n-i):
        print('*',end=" ")
    print()

#right triangle with odd element 

n=3
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print('*',end=" ")
    k=k+2
    print()


#pyramid 
#method1 
n= 4
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
#method 2 --using concatenation


def diamond(n):
    #for top triangle
    for i in range(0,n):
        print(" "*(n-i)+ " *"*(i+1))
    #for down triangle
    for j in range(0,n-1):
        print(" "*(j+2)+" *"*(n-1-j))
print(diamond(4))

