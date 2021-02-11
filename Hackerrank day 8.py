import sys

n = int(input())
arr2 = []
for i in range(n):
    arr = list(map(str, input().lower().split()))
    arr2.append(arr)

u = 0
r = 0
k = n
arr3 = []
l = input()
x=1
for q in range (x):
    arr3.append(l)
    l=input()








w = len(arr3)
p = 0
for z in range(w):
    while k > 0:

        if arr3[r] == arr2[u][0]:
            print(arr2[u][0], end='')
            print('=', end='')
            print(arr2[u][1])


        else:
            p = p + 1
        u = u + 1
        k = k - 1

    if p == n:
        print('Not found')
    k = n
    u = 0
    p = 0
    w = w + 1
    r = r + 1
