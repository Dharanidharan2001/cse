def transpose(arr):

    for i in range(len(arr)):
       for j in range(len(arr)):
          b[i][j] = arr[j][i]
          print(b[i][j],end=' ')
       print()

#using nested list
# m = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
# for r in m:
#     print(r)
b=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
arr=[[1,2,3,2],[3,4,2,1],[5,3,2,1],[6,7,5,3]]
transpose(arr)
