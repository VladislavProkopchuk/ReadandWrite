import os

def read_file(file):
    with open(file, 'r') as f:
        content = f.readlines()
    return content, len(content)
files = [file for file in os.listdir('.') if file.endswith('.txt')]
file_contents = []
for file in files:
    content, num_lines = read_file(file)
    file_contents.append((file, num_lines, content))
file_contents.sort(key=lambda x: x[1])
result_content = []
for file in file_contents:
    result_content.append(file[0])
    result_content.append(str(file[1]))
    result_content.extend(file[2])
with open('result.txt', 'w') as f:
    f.write('\n'.join(result_content))