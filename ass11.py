import re
fd=r'/Users/kimjinhyuk/Desktop/py4e/regex_sum_1591335.txt'
f = open(fd)
f_read=f.read()
intlist=re.findall('[0-9]+',f_read)
temp=0

for i in range(len(intlist)):
    temp= temp+int(intlist[i])

print(temp)