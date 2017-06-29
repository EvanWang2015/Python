fname = input("Enter file name:")
fh = open(fname)
lst = list()
for line in fh:
    words = line.strip().split()
    for indi in words:
        if indi not in lst:
            lst.append(indi)
lst.sort()
print (lst)