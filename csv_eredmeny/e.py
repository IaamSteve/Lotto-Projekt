from os import system
from func import *
system('cls')
''' Előző heti eredmények '''
hely = input("Kérek egy felhasználónevet: ")
tomb = beolvas(hely)
print("Heti eredmények")
print(tomb[0:2])
''' Legtöbb előfordulás '''
print("Legtöbb előfordulás")
db = 0
sorsonly = []
le_tomb = []
for x in tomb:
    for z in x[1]:
        sorsonly.append(z)
for y in range(1,100):
    t = []
    db = 0
    for x in sorsonly:
        if x==y:
            db+=1
    t.append(y)
    t.append(db)
    le_tomb.append(t)
print(sorted(le_tomb, key=lambda x: x[1], reverse=True)[0:3])
del le_tomb
''' Legkisebb összeg '''
print("Legkisebb összegek")
print(sorted(tomb, key=lambda x: x[2])[0:3])
''' Hasonló számsorok '''
print("Hasonló számsorok")
for x in tomb:
    for y in tomb:
        if (y!=x):
            db = 0
            for z in range(5):
                if x[1].count(y[1][z])>0:
                    db+=1
            if db>3:
                print(y,x)
del t
''' Sorozatok '''
print("Sorozatok")
t = []
for x in tomb:
    for y in range(1,25):
        db = 0
        if x[1][0]+y==x[1][1]:
            db+=1
            if x[1][1]+y==x[1][2]:
                db+=1
                if x[1][2]+y==x[1][3]:
                    db+=1
                    if x[1][3]+y==x[1][4]:
                        db+=1
        if db>2:
            print(x[1])