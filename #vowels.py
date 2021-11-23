import re
m = 'To be, or not to be, that is the question'
vow=re.findall("e|u|o|a|i",m)
print(len(vow))