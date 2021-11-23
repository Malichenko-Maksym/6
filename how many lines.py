i=0
k=input('file name? ')
with open(k) as f:
    for line in f: i+=1
print(f'File name: {k}')
print(f'Number of lines: {i}')