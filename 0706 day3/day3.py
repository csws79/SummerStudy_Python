refri = {}
f = open("refri.txt", 'r')
a = f.readline()
#key1, value1 = a.split()
#refri[key1] = int(value1)

def show():
    f = open("refri.txt", 'r')
    for i in f.readlines():
        key1, value1 = i.split()
        print key1 + " " + str(value1)
    save()

def add(new, x):
    if(new in refri):
        refri[new] += x
        save()
    elif(new not in refri):
        refri[new] = x
        save()

def delete(dele, y):
    if(dele in refri):
        if(refri[dele] > y):
            refri[dele] -= y
            save()
        elif(refri[dele] == y):
            del refri[dele]
            save()
        elif(refri[dele] < y):
            print "you cannot do this. amount to delete is too much."
    elif(dele not in refri):
        print "you cannot do this. the stuff does not exist in refri."

def save():
    f = open("refri.txt", 'w')
    #f.write(str(refri.keys) + " " + str(refri.values) + "\n")
    for i in (refri.keys()):
        f.write(i + " " + str(refri[i]) + "\n")


while True:
    print "1. show list, 2. add stuff, 3. delete stuff, 4. save all data and shut the refri"

    n = input("input number 1, 2, 3, or 4: ")
    if(n == 1):
        show()
        continue

    elif(n == 2):
        new = raw_input("input your stuff name to deposit: ")
        x = input("input your stuff amount to deposit: ")
        add(new, x)
        continue

    elif(n == 3):
        dele = raw_input("input your stuff name to withdraw: ")
        y = input("input your stuff amount to withdraw: ")
        delete(dele, y)
        continue

    elif(n == 4):
        print "all data is saved in refri.txt. refri is shut."
        save()
        break

    else:
        print "you did input wrong number. input number 1, 2, 3, or 4: "