import random

ans1 = 0
ans2 = 0
ans3 = 0

while True:
    l = random.randint(1, 9)
    m = random.randint(1, 9)
    n = random.randint(1, 9)

    if l == m or m == n or n == l :
        continue
    elif l != m and m != n and n != l :
        answer = (l, m, n)
    break

#print answer



while True:
    strike = 0
    ball = 0
    ans1 = input()
    ans2 = input()
    ans3 = input()

    for i in (answer):
        if(ans1 in answer):
            if(ans1 == answer[0]):
                strike += 1
            else:
                ball += 1
        if(ans2 in answer):
            if(ans2 == answer[1]):
                strike += 1
            else:
                ball += 1
        if(ans3 in answer):
            if(ans3 == answer[2]):
                strike += 1
            else:
                ball += 1

    print str(strike / 3) + " strike " + str(ball / 3) + " ball"
    if(strike / 3 == 3):
        print "Answer: " + str(answer)
        break