name = input("Enter file name:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if line.startswith('From'):
        ele = line.strip().split()
        if len(ele)>5:
            dic[ele[1]]= dic.get(ele[1],0) + 1
bigCount = None
bigEmail = None
for word, count in dic.items():
    if bigCount is None or bigCount < count:
        bigCount = count
        bigEmail = word
print (bigEmail, bigCount)       