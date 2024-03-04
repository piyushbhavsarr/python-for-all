
binary_file_path = 'image.jpg'

with open(binary_file_path, 'rb') as binary_file:
    binary_data = binary_file.read()

new_binary_file_path = 'image_copy.jpg'
with open(new_binary_file_path, 'wb') as new_binary_file:
    new_binary_file.write(binary_data)
