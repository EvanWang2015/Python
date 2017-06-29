import re
print (sum([int(x) for x in re.findall('[0-9]+',open("regex_sum_379437.txt").read())]))
#name = "regex_sum_379437.txt"
#handler = open(name)
#data = handler.read()
#lis = re.findall('[0-9]+',data)
#numlist = [int(x) for x in lis]
#print(len(numlist))
#print (re.findall('[0-9]+',data))
#print (sum(numlist))
#print (sum([int(x) for x in re.findall('[0-9]+',open("regex_sum_379437.txt").read())]))