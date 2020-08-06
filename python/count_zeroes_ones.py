def count(arr):
    # Write your code here
    count0 = 0
    count1 = 0
    for x in arr:
        for y in x:
            if y == 0:
                count0 += 1
            if y == 1:
                count1 += 1
    print(count0)
    print(count1)        

input=[[1,0,0,1],[0,1,0,1],[1,1,0,1]]
count(input)
# input2=[[1,0,1,1],[0,1,0,0],[1,1,0,1]]
# count(input2)
