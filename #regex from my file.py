import re
f = open("fileee.txt")
k=f.read()
f.close()
z=re.sub("\w*\d\w+",'',k)
words=re.findall("\w\w\w\w\w\w+",z)
for i in words: print(i)

#print(re.findall("\w*\d\w+",k))