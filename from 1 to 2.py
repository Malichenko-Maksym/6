k=input('file name? ')
with open(k) as f:
    z=f.read()
with open('copy.txt', 'w') as q:
    q.write(z)