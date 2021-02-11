Scatteredarray=[1]
x=3
n=2
while len(Scatteredarray)<50001:
    Scatteredarray.append(x)
    x=x+2
while len(Scatteredarray)<100000:
    Scatteredarray.append(n)
    n=n+2
print(len(Scatteredarray))
print(Scatteredarray[50001])
#the above code created an array of 100000 scattered numbers odd one side even one side


Sortedarray=(sorted(Scatteredarray))
#the above code sorts the scattered numbers
print(len(Sortedarray))
print(Sortedarray[50001])