#List and Operations on it.
first_list = []
n=5
for i in range (0,n):
    inp = input("Enter Data to enter in the list :")
    first_list.append(inp)

print(first_list)

#iterable

second_list = ['Game', 'Screen', 'Javascript', 'WebApps', 200, 400, 405]

print(second_list)
print("Merging both first + second")
first_list.extend(second_list)
print(first_list)

#list.insert(i, x) -> index, value

first_list.insert(10, "inserted value")
print(first_list)

