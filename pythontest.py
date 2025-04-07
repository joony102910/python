i,k,gob,dan = 0,0,0,""

for i in range(2,10):
    dan = dan + ("# %d단 # " %i)
print(dan)

for i in range(1,10):
    dan = ""    
    for k in range(2,10):
        gob = i*k
        dan = dan + str("%2dX%2d=%2d" %(k,i,gob))
    print(dan)