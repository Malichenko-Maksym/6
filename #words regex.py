import re
m = 'To be, or not to be, that is the question'
words=re.findall("\w+",m)
print(len(words))