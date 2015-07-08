subject = {}
f = open("subject.txt", 'r')
for i in f.readlines():
    keys, value = i.split()
    subject[keys] = int(value)

user = []
userData = []
u = open("user.txt", 'r')
#print u.readlines()
while(True):
    s = u.readline()
    if s == "":
        break
    userData2 = s.split()
    user.append(userData2)
#print user
#print userData
print user
def show():
    f = open("subject.txt", 'r')
    for i in f.readlines():
        key1, value1 = i.split()
        print key1 + " " + str(value1)

def username(us):
    if(us not in user):
        print "This username does not exist in user.txt."
    elif(us in user):
        pass


def apply(code):
    if(code not in subject):
        print "This subject code does not exist in subject.txt."
     #elif(code in subject):

def delete(code):
    if(code not in subject):
        print "This subject code does not exist in subject.txt."
    #elif(code in subject):

    for a in user:
        n = user.find(code)
        del n
        return
    print "wrong subject code."


def userShow(us):
    for a in user:
        if a[0] != us:
            pass
        elif a[0] == us:
            print a
            return
    print "wrong username."

while(True):
    print "1. show subject list, 2. apply subject, 3. cancel applying, 4. show applying list, 5. save data and exit program"

    n = input("Input number 1, 2, 3, 4, or 5: ")
    if(n == 1):
        show()
        continue
    elif(n == 2):
        us = raw_input("Input username: ")
        code = input("Input subject code: ")
        userShow(us)
        apply(code)
        continue
    elif(n == 3):
        us = raw_input("Input username: ")
        userShow(us)
        us = input("Input subject code: ")
        delete(code)
        continue
    elif(n == 4):
        us = raw_input("Input username: ")
        userShow(us)
        continue
    elif(n == 5):
        print "Exit program"
        break