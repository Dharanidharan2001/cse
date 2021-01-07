def compare(a,b):

    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    li = [alice,bob]
    return li

a=[2,3,8]
b=[1,3,9]
#a = list(map(int,input().split( )))
#b = list(map(int,input().split( )))

result = compare(a,b)
print(result)
