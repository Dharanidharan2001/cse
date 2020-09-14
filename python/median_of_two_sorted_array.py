def med_of_two_sorted(x,y):

    l=x+y
    n= len(l)

    if n % 2 == 0:
        med1 = l[n//2]
        med2 = l[n//2 - 1]
        median = (med1+med2)/2
    else:
        median = l[n//2]

    return ("the median of the given arrays is {}".format(median))


x = list(map(int, input().rstrip().split()))
y = list(map(int, input().rstrip().split()))
print(med_of_two_sorted(x,y))
