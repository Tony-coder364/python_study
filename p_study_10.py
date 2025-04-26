#matrix


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

output=[]

left,right,top,bottom=0,len(a[0]),0,len(a)
while True:
    for i in range(left,right):
        output.append(a[top][i])
    top+=1


    for j in range(top,bottom):
        output.append(a[j][right-1])
    right-=1

    if left!=right and top!=bottom:
        for k in range(right-1,left-1,-1):
            output.append(a[bottom-1][k])
        bottom-=1

        for l in range(bottom-1,top-1,-1):
            output.append(a[l][left])
        left+=1
    else:
        break
print(output)