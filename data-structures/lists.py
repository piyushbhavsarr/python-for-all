#List and Operations on it.
first_list = []
n=4
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

#list.remove(x) , here value which has to be removed must be entered.
second_list.remove('Game') # Game is removed from the second list
print(second_list)

#list.pop(i) Remove the item at the given position in the list *square brackets should not be used

second_list.pop() #if nothing is there, last elements is deleted
print(second_list)

second_list.pop(3) #remove the item present at the index location 3
print(second_list)

#list.index(x[, start[, end]])

my_list = ['apple', 'banana', 'orange', 'banana', 'grape']

# Find the index of the first occurrence of 'banana'
index = my_list.index('banana')
print(f"Index of 'banana': {index}")

# Find the index of 'banana' starting from index 2
index_starting_from_2 = my_list.index('grape', 2)
print(f"Index of 'banana' starting from index 2: {index_starting_from_2}")

# Find the index of 'banana' between index 2 (inclusive) and 4 (exclusive)
index_within_range = my_list.index('banana', 0, 4)
print(f"Index of 'banana' within the range [2, 4): {index_within_range}")