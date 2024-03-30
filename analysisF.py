path='LogB.strace'
file=open(path)
lines2=file.readlines()
count=0
term1=' read('
term2='tty'
term3='pipe'
for i in lines2:
    if term1 in i and term2 not in i and term3 not in i:
        print(i)
        count+=1
print(count)
