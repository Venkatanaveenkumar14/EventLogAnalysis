# A strace -Keystrokes
path='LogA.strace'
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


#id
#uname -a
#head te
#use tail user
#echo [Dabcdefg]
#C - cancel
#use
#head use