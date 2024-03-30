# B strace
path='LogB.strace'
file=open(path)
lines=file.readlines()
count=0
term=' read('
for i in lines:
    if term in i:
        print(i)
        count+=1
print(count)