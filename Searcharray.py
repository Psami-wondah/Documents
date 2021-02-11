array1=[1]
x=2
while len(array1)<100000:
    array1.append(x)
    x=x+1
print(len(array1))


r=input('enter the value to be searched for in array1\n')
r=int(r)

def searcharray(r):
    c=0
    while array1[c] != r and array1[c] < 100000:
        c=c+1
    if array1[c] == r:
        print('The value', r, 'is at array location array1[',  c, ']')
    else:
        print("The value doesn't exist in array1")

searcharray(r)


#written by Owhondah Okechukwu Samuel





