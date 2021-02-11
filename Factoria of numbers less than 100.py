x=input('Enter a whole number less than 100 to get its factoria\n')
x=int(x)
n=x

if x<100 and x>1 :
    while(n>1):
        x= x * (n - 1)
        n=n-1

elif x==1:
    x=1
elif x==0:
    x=0
else:
    print('number must be a whole number and must be less than 100')


print(x)