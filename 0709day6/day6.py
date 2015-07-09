#-*- coding:utf-8 -*-
#파일 입출력 및 예외처리 예제
try:
    fileOpen = raw_input()
    open(fileOpen, 'r')
except IOError:
    print "not found"
finally:
    f = open(fileOpen, 'a+')
    print f.readline()
    a=raw_input()
    f.write(a)
    f.close()