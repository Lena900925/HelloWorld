door = []

for visit in range(100):
    door.append(False)

def opened(num):
    if num <= 100:
        for visit in range(100):
            if (visit+1) % num == 0:
                if door[visit] == False:
                    door[visit] = True
                else:
                    door[visit] = False
        num += 1
        opened(num)
def res():
    res=[]
    for visit in range(100):
        if door[visit] == True:
            res.append(visit+1)
    print("The following doors are open: ", res)

opened(1)
res()