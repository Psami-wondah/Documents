n="{0:b}".format(int(input().strip()))

a = max(n.split('0')).count('1')
print(a)