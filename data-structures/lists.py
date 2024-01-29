#List and Operations on it.
first_list = []
n=10
for i in range (0,n):
    inp = input("Enter Data to enter in the list :")
    first_list.append(inp)

print(first_list)

#iterable

second_list = ['Game', 'Screen', 'Javascript', 'WebApps', 200, 400, 405]

print(second_list)
print("Merging both first + second")
c = first_list.extend(second_list)
print(c)
