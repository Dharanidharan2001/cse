def two_sum(a):
    start = 0
    end = len(a)-1
    target = 9
    while start < end:
        s = a[start] + a[end]
        if s == target:
            print(a[start],a[end])
            return True
        elif s < target:
            start = start+1
        else:
            end = end-1
    return False

a=[1,2,3,4,5]
print(two_sum(a))