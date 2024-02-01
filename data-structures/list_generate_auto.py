# Generate numeric list using range
numeric_list = list(range(1, 11))  # Numbers from 1 to 10

print("Numeric List:", numeric_list)
#Numeric List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Generate alphanumeric list with integer digits

import random
import string


alphanumeric_list = [random.choice(string.ascii_letters) + (random.randint(0, 9)) for _ in range(10)]

print("Alphanumeric List with Integer Digits:", alphanumeric_list)
#-> Alphanumeric List with Integer Digits: ['L2', 'Y8', 'H0', 'H0', 'j7', 'd5', 'h5', 'Z2', 'U0', 'E0']


# Generate a list with a mix of uppercase letters, lowercase letters, and integers

import random
import string

result_list = [random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) if random.random() < 0.5 else random.randint(1, 1000) for _ in range(10)]

print("Generated List:", result_list)
#-> Generated List: ['C', 434, 100, '8', 202, 24, 214, 'j', 322, 'H']
