arr=[]
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))
n=0
m=0
final=[]
for l in range(4):
    for j in range(4):
        k= arr[n][m] + arr[n][m+1]+ arr[n][m+2]+ arr[n+1][m+1]+ arr[n+2][m]+ arr[n+2][m+1]+ arr[n+2][m+2]
        final.append(k)
        m=m+1
    m=0
    n=n+1
print(max(final))
    