path='LogA.strace'
file=open(path)
lines1=file.readlines()
count=0
term1=' read('
term2='tty'
term3='pipe'
for i in lines1:
    if term1 in i and term2 not in i and term3 not in i:
        print(i)
        count+=1
print(count)

#deleted user_file.txt
#echo abcdefg - acknowledged by echoing abcefg after deleting user_file.txt
