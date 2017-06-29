largest = None
smallest = None
while True:
    inp = input("Enter the number: ")
    if inp == "done":
        break
    try: num = int(inp)
    except:
        print ("Invalid input")
        continue
    if largest is None:
        largest = num
    if largest < num:
        larget = num
    if smallest is None:
        smallest = num
    if smallest > num:
        smallest = num
print ("Maximum is", largest)
        