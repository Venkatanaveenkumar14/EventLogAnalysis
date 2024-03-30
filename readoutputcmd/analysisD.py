# B strace -Keystrokes
path='LogB.strace'
file=open(path)
lines=file.readlines()
count=0
term1=' read('
term2='tty'
for i in lines:
    if term1 in i and term2 in i:
        print(i)
        count+=1
print(count)