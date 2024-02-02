def main():
    # List
    numbers = [1, 2, 3, 4, 5]
    print("List:", numbers)

    # Tuple
    fruits = ('apple', 'banana', 'orange')
    print("Tuple:", fruits)

    # Set
    colors = {'red', 'green', 'blue'}
    print("Set:", colors)

    # Dictionary
    student_info = {'name': 'John', 'age': 20, 'grade': 'A'}
    print("Dictionary:", student_info)

    # String
    sentence = "This is a sample sentence."
    print("String:", sentence)

    # Accessing elements in data structures
    try:
        print("First element in List:", numbers[0])
        #append the list
        numbers.append(6)
        #reverse the list
        print(numbers)
        numbers.reverse()
        print(numbers)
        print("Second element in Tuple:", fruits[1])
        print("Element in Set:", next(iter(colors)))
        print("Value in Dictionary:", student_info['age'])
        print("Substring in String:", sentence[5:11])
        
        # Handling index out of range error
        print("Invalid index in List:", numbers[4])

    except IndexError as e:
        print("Index Error:", e)

    # Handling key error in dictionary
    try:
        print("Non-existing key in Dictionary:", student_info['age'])
    except KeyError as e:
        print("Key Error:", e)

if __name__ == "__main__":
    main()