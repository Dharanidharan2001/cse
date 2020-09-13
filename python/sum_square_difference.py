sum_square = 0
sum = 0
for i in range(1,101):
    sum += i
    sum_square += i**2
    diff = sum**2 - sum_square

# print(sum)
# print(sum_square)
print(diff)