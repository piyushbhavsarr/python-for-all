import io

#with text data
text_data = "Hello, this is text data."
text_stream = io.StringIO(text_data)

#with binary data
binary_data = b'\x48\x65\x6c\x6c\x6f'
binary_stream = io.BytesIO(binary_data)
