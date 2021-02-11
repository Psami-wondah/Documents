n = int(input())
my_dict = {}
for x in range(n):
    name, number = input().split()
    my_dict[name] = int(number)

# store and retrieve names
names = []

user_input = input()
while len(user_input) != 0:
    names.append(user_input)
    user_input = input()

for i in names:
    if i in my_dict.keys():
        print(f'{i}={my_dict[i]}')
    else:
        print('Not found')