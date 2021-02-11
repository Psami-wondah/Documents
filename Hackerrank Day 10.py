n="{0:b}".format(int(input().strip())).split()
k=0
r=0
binlist =[]

for i in range(len(n)):
    if n[r] == '1':
        k=k+1
    elif n[r] == '0':
        binlist.append(k)
        k=0
    r=r+1

binlist.append(k)
print(max(binlist))