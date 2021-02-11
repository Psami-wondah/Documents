n= int(input())
Phonebook ={}
for i in range(n):
    namesnumbers = list(map(str, input().lower().split()))
    Phonebook[namesnumbers[0]] = namesnumbers[1]
while True:

    try:
        name = input()
        if name in Phonebook:
            print(name+ '=' +Phonebook[name] )
        else:
            print('Not found')
    except EOFError:
        break