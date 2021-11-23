import random
f = open("integersrand.txt","w")
f.close()
f = open("integersrand.txt","a")
for i in range(1,51):
    k=random.randrange(100,1000)
    f.write(f'{k} \n')
f.close()