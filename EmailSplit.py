fname = input("Enter file name: ")
if len(fname) <1: fname = "mbox-short.txt"
fh = open(fname)
count = 0
lis = list()
for line in fh:
    if line.startswith('From'):
        ele = line.strip().split()
        if len(ele) >5:
            lis.append(ele[1])
            count = count + 1
            print (ele[1])
print ("There were", count, "lines in the file with From as the first world" )