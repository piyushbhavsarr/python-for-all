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
print(f"Index of 'banana' within the range 2 (inclusive) and 4 (exclusive) : {index_within_range}")

#list.clear()
second_list.clear()

#list.count(x)
my_list.count('banana')

my_list = ['apple', 'banana', 'orange', 'banana', 'grape']

# Using list comprehension to find indexes of 'banana'
banana_indexes = [index for index, value in enumerate(my_list) if value == 'banana']

print(f"Indexes of 'banana': {banana_indexes}")

#sorting

#simple sorting -numbers
list_a = [1,3,2,9,6,1,5,4,1,10,15,54,69,45]
print(f"list a is : {list_a}")
list_a.sort()
print(list_a)
#list a is :  [1, 3, 2, 9, 6, 1, 5, 4, 1, 10, 15, 54, 69, 45]
#[69, 54, 45, 15, 10, 9, 6, 5, 4, 3, 2, 1, 1, 1]



#Using words - alphabets.
list_a = ['zip','z','ball','python','apple','boat','table','t','a']
print("list a is : ",list_a)
list_a.sort()
print(list_a)
# list a is :  ['zip', 'z', 'ball', 'python', 'apple', 'boat', 'table', 't', 'a']
# ['a', 'apple', 'ball', 'boat', 'python', 't', 'table', 'z', 'zip']



#testing on both alphabets and number - i.e. alphanumeric lists with string format
list_a = ['a','1','A','0123','0','01','0a']
print("list a is : ",list_a)
list_a.sort()
print(list_a)

# list a is :  ['zip', 'z', 'ball', 'python', 'apple', 'boat', 'table', 't', 'a']
# ['a', 'apple', 'ball', 'boat', 'python', 't', 'table', 'z', 'zip']


#testing on both alphabets and number - i.e. alphanumeric lists with mixed format
#list_a = [2, '2']
print("list a is : ",list_a)
list_a.sort()
print(list_a)
#ERROR '<' not supported between instances of 'str' and 'int'

#Explore more (custom sort)
#list.sort(key=None,reverse=False)
print("Custom Sorting Lists")

def custom_sort(string):
    return len(string)

list_b = ['apple','banana','apple','watermelon','laptop','ubuntu']
list_b.sort(key = custom_sort)
print(list_b)

#if the lists is numeric:
def custom_sort(string):
    return len(str(string))

list_b = [1,2,3,4,5,3,344,443]
list_b.sort(key = custom_sort)
print(list_b)

#Sorting with lambda function:
list_b = ['python','java','javascript','nodejs','reactjs','angular']

# Sort the list based on the last character of each word

list_b.sort(key = lambda x:x[-1])   
print(list_b) #['java', 'python', 'angular', 'nodejs', 'reactjs', 'javascript']

#list.reverse

list_b.reverse()
print("reversed ",list_b)

#list.copy() - it is a shallow copy.
copied_list = list_b.copy()
print("copied new list ", copied_list)



