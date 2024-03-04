from contextlib import contextmanager

@contextmanager
def open_file(file_path, mode='r'):
    file = open(file_path, mode)
    try:
        yield file
    finally:
        file.close()

#usage
with open_file('example.txt', 'r') as file:
    content = file.read()
    print(content)
