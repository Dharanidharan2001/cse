# def count(arr):
    # Write your code here
    # count0 = 0
    # count1 = 0
    # for row in arr:
    #     for element in row:
    #         if element == 0:
    #             count0 += 1
    #         if element == 1:
    #             count1 += 1
    # print(count0)
    # print(count1)
    #


"""
Access 1D arr:
for i in range(0, len(arr)):
    print(arr[i])

2D array:
arr[0][0]
arr[0][1]
"""
def count(arr):
    count = 0
    for i in range(0,len(arr)):
        for j in arr[i]:
            if j == 1:
               count += 1
    print(count)
inp = [[1,2,3,2],[2,1,2,3]]
print(count(inp))


# input=[[1,0,0,1],[0,1,0,1],[1,1,0,1]]
# count(input)
# input2=[[1,0,1,1],[0,1,0,0],[1,1,0,1]]
# count(input2)
