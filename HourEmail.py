name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
dic = dict()
handle = open(name)
for line in handle:
    if line.startswith('From'):
        ele = line.split()
        if len(ele)>5:
            
            hourString = str(ele[5])           
            #hour = hourString[2:4]
            hour = hourString.split(':',1)[0]
            #print(hour)
            dic[hour] = dic.get(hour,0)+1
lst = list()
for key, val in dic.items():
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print (key, val)