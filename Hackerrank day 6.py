T=int(input())
for i in range(T):
    S=str(input())
    n=len(S)
    l=n//2
    k=l
    x=0
    b=1
    if l<(n/2):
        l=l+1
    for j in range(l):
        print(S[x], end='')
        x=x+2

    print(' ', end='')

    for u in range(k):
        print(S[b], end='')
        b=b+2

    print('')

