arr= [[1,2,3,4],[2,3,4,5],[4,5,7,5],[2,8,9,8]]
b=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# m = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
# for r in m:
#     print(r)


for i in range(len(arr)):
    for j in range(len(arr)):
        b[i][j] = arr[j][i]
        print(b[i][j],end=' ')
    print()
