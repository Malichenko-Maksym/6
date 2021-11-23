f = open("powers.txt","w")
f.close()
f = open("powers.txt","a")
for i in range(1,11):
  f.write(f'{i},{i**2},{i**3}\n')
f.close()