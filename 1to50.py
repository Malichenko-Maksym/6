f = open("integers.txt","w")
f.close()
f = open("integers.txt","a")
for i in range(1,51):
    f.write(f'{i} \n')
f.close()