import re
f = open("grades.txt")
k=f.read()
f.close()
words=re.findall("\d\.\d",k)
s=0
for i in words: s+=float(i)
print(s)

