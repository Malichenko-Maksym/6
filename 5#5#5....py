

def fil(q):
    f = open(q)
    while True:
        for i in range(5):
            z=f.readline()
            if z=='': return 0
            print(z, end='')
        input('enter to next 5 lines')
    f.close()
k=input('file name? ')
fil(k)    
