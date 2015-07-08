refri = {'kimchi' : 10, 'bibimbap' : 5}

while True:
    print "1. show list, 2. add stuff, 3. delete stuff, 4. shut the refri"

    n = input("input number 1, 2, 3, or 4: ")
    if(n == 1):
        print refri
        continue

    elif(n == 2):
        new = raw_input("input your stuff name to add: ")
        x = input("input your stuff amount to add: ")
        if(new in refri):
            refri[new] += x
        elif(new not in refri):
            refri[new] = x
        continue

    elif(n == 3):
        dele = raw_input("input your stuff name to delete: ")
        y = input("input your stuff amount to delete: ")
        if(dele in refri):
            if(refri[dele] > y):
                refri[dele] -= y
            elif(refri[dele] == y):
                del refri[dele]
            elif(refri[dele] < y):
                print "you cannot do this. amount to delete is too much."
        elif(dele not in refri):
            print "you cannot do this. the stuff do not exist in refri."
        continue

    elif(n == 4):
        print "refri is shut."
        break

    else:
        print "you did not input wrong number. input number 1, 2, 3, or 4."