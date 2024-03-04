def process_chunk(chunk, keyword_counts):
    lines = chunk.split('\n') #splitting into lines

    for line in lines: #counting the occurneces of specific keywords
        for keyword in keyword_counts:
            if keyword in line:
                keyword_counts[keyword] += 1

keyword_counts = {'error': 0, 'warning': 0, 'info': 0}

chunk_size = 1024  # 1 KB

with open('large_log_file.txt', 'r') as log_file:
    while chunk := log_file.read(chunk_size):
        process_chunk(chunk, keyword_counts)

# Print the final keyword counts
print("Keyword Counts:")
for keyword, count in keyword_counts.items():
    print(f"{keyword}: {count}")
