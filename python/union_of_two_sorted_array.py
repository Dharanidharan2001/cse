def union(n1,n2,m,n):
    i=0
    j=0

    while i < m and j < n:

        if n1[i] > n2[j]:
            print(n1[i])
            i+=1
        elif n1[i] < n2[j]:
            print(n2[j])
            j+=1
        else:
            print(n1[i])
            i+=1
            j+=1

    while i < m:
        print(n1[i])
        i+=1
    while j < n:
        print(n2[j])
        j+=1

n1=[1,2,3,4,5]
n2=[2,3,4,6]
m = len(n1)
n = len(n2)
print(union(n1,n2,m,n))
