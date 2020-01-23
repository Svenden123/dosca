import time
import random
import sys

def create_random():
    m, n = 10, 10
    doska = []
    doska.append([2 for i in range(m+2)])
    for i in range(n):
        doska.append([2] + [int(random.randint(0,1)) for i in range(m)] +[2])
    doska.append([2 for i in range(m+2)])
    return doska

def pr_doska():
    for i in range(1,len(doska)-1):
        for j in range(1, len(doska[i])-1):
            print(doska[i][j], end=' ')
        print()
    print()

if (len(sys.argv) < 2):
    print("""Usage the following syntax:
./script.py 0 path_to_file
    for read from a file
./script.py 1
    for generation random data """ )
    exit(0)
elif (sys.argv[1] == '0'):
    f = open(sys.argv[2],'r')
    doska = []
    mas_chit = []
    for i in f:
        mas_chit.append([int(j) for j in i.split()])
    doska.append([2 for i in range(len(mas_chit[0])+2)])
    for i in range(len(mas_chit)):
        doska.append([2] + mas_chit[i] +[2])
    doska.append([2 for i in range(len(mas_chit[0])+2)])
    pr_doska()
elif (sys.argv[1] == '1'):
    doska = create_random()

def change(doska):
    count = 0
    for i in range(1,len(doska)-1):
        for j in range(1, len(doska[i])-1):
            
            if(doska[i-1][j-1] == 1):
                count+=1
            if(doska[i-1][j] == 1):
                count+=1
            if(doska[i-1][j+1] == 1):
                count+=1
            if(doska[i][j-1] == 1):
                count+=1
            if(doska[i][j+1] == 1):
                count+=1
            if(doska[i+1][j-1] == 1):
                count+=1
            if(doska[i+1][j] == 1):
                count+=1
            if(doska[i+1][j+1] == 1):
                count+=1
            
            if (doska[i][j] == 1):
                if count < 2:
                    doska[i][j] = 0
                elif count <=3:
                    pass
                else:
                    doska[i][j] = 0
            else:
                if count == 3:
                    doska[i][j] = 1

            count = 0

while(True):
    time.sleep(1)
    change(doska)
    pr_doska()