

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps=0


while True:
    numberOfSwaps = 0

    for j in range(0, n - 1):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps = numberOfSwaps + 1


    if (numberOfSwaps==0):
        break
    numSwaps= numSwaps + numberOfSwaps



print(f'Array is sorted in {numSwaps} swaps.')
print('First Element:', a[0])
print('Last Element:', a[n-1])