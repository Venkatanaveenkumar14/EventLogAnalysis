path='OutputE.txt'
file=open(path)
lines=file.readlines()
file_names = []
counts = []
for i in lines:
    file_name_start = i.find('<')
    file_name_end = i.find('>')
    file_name = i[file_name_start + 1:file_name_end]
    if file_name not in file_names:
        file_names.append(file_name)
        idx = file_names.index(file_name)
        counts.append(1)
    else:
        idx = file_names.index(file_name)
        counts[idx] += 1
print("File Name\t\t\t\t\t\tTotal Reads")
print("________________________________________________________________________")
for i in range(len(file_names)):
    print(f"{file_names[i]}\t\t\t{counts[i]}")