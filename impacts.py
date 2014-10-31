#!/usr/bin/python

import random

SIZE = 50
craterSize = SIZE/10
craters = [0]
time = 0
crater = 0.0
EMPTY = '|'
CENTER = 'X'
CRATER = ' '
DEBRIS = '-'

grid = [[EMPTY for x in xrange(SIZE)] for x in xrange(SIZE)]


def numCraters(grid):
    crater = 0
    for i in range(SIZE-1):
        for j in range(SIZE-1):
            if(grid[i][j] == CENTER):
                crater += 1.0
    return crater

def makeImpact(grid):
    imp_i = random.randrange(0, SIZE-1)
    imp_j = random.randrange(0, SIZE-1)
    #print("imp_i: ", imp_i, " imp_j: ", imp_j)

    for i in range((craterSize/2)+2):
        for j in range(((craterSize/2)+2)-i):
            if(imp_i+i >= SIZE):
                if(imp_j+j >= SIZE):
                    grid[imp_i][imp_j-j] = DEBRIS
                    grid[imp_i-i][imp_j-j] = DEBRIS
                    grid[imp_i-i][imp_j] = DEBRIS
                if(imp_j-j <= 0):
                    grid[imp_i][imp_j+j] = DEBRIS
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS
                if(imp_j+j < SIZE and imp_j-j > 0):
                    if(imp_j+j >= SIZE): print SIZE
                    #print "imp_j+j: ", imp_j+j
                    grid[imp_i][imp_j-j] = DEBRIS
                    grid[imp_i][imp_j+j] = DEBRIS
                    grid[imp_i-i][imp_j-j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS

            if(imp_i - i < 0):
                if(imp_j+j >= SIZE):
                    grid[imp_i][imp_j-j] = DEBRIS
                    grid[imp_i+i][imp_j-j] = DEBRIS
                    grid[imp_i+i][imp_j] = DEBRIS
                if(imp_j-j < 0):                         
                    grid[imp_i][imp_j+j] = DEBRIS
                    grid[imp_i+i][imp_j] = DEBRIS
                    grid[imp_i+i][imp_j+j] = DEBRIS
                if(imp_j+j < SIZE and imp_j-j>0):                
                    if(imp_j+j >= SIZE): print SIZE
                    #print "imp_j+j: ", imp_j+j
                    grid[imp_i][imp_j-j] = DEBRIS
                    grid[imp_i][imp_j+j] = DEBRIS
                    grid[imp_i+i][imp_j-j] = DEBRIS
                    grid[imp_i+i][imp_j+j] = DEBRIS
                        
            if(imp_j+j >= SIZE):
                if(imp_i+i >= SIZE):
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j-j] = DEBRIS
                    grid[imp_i][imp_j-j] = DEBRIS

                if(imp_i-i <= 0):
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j-j] = DEBRIS
                    grid[imp_i][imp_j-j] = DEBRIS

                if((imp_i+i < SIZE) and imp_i-i >0):
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i+i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j-j] = DEBRIS
                    grid[imp_i+i][imp_j-j] = DEBRIS

            if(imp_j-j <= 0):
                if(imp_i+i >= SIZE):                    
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS
                    grid[imp_i][imp_j+j] = DEBRIS
                if(imp_i-i <= 0):
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS
                    grid[imp_i][imp_j+j] = DEBRIS
                if(imp_i+i < SIZE and imp_i-i>0):
                    #print "imp_i+i: ", imp_i+i
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i+i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS
                    grid[imp_i+i][imp_j+j] = DEBRIS     
           
            if(imp_j+j < SIZE and imp_j-j >=0 and imp_i +i < SIZE and imp_i - i >=0):
                grid[imp_i-i][imp_j-j] = DEBRIS
                grid[imp_i+i][imp_j-j] = DEBRIS
                grid[imp_i-i][imp_j +j] = DEBRIS
                grid[imp_i+i][imp_j +j] = DEBRIS

    for i in range((craterSize/2)+1):
        for j in range(((craterSize/2)+1)-i):
            if(imp_i+i >= SIZE):
                if(imp_j+j >= SIZE):
                    grid[imp_i][imp_j-j] = CRATER
                    grid[imp_i-i][imp_j-j] = CRATER
                    grid[imp_i-i][imp_j] = CRATER
                if(imp_j-j <= 0):
                    grid[imp_i][imp_j+j] = CRATER
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i-i][imp_j+j] = CRATER
                if(imp_j+j < SIZE and imp_j-j>0):
                    #if(imp_j+j >= SIZE): print SIZE
                    #print "imp_j+j: ", imp_j+j
                    grid[imp_i][imp_j-j] = CRATER
                    grid[imp_i][imp_j+j] = CRATER
                    grid[imp_i-i][imp_j-j] = CRATER
                    grid[imp_i-i][imp_j+j] = CRATER

            if(imp_i - i < 0):
                if(imp_j+j >= SIZE):
                    grid[imp_i][imp_j-j] = CRATER
                    grid[imp_i+i][imp_j-j] = CRATER
                    grid[imp_i+i][imp_j] = CRATER
                if(imp_j-j < 0):                         
                    grid[imp_i][imp_j+j] = CRATER
                    grid[imp_i+i][imp_j] = CRATER
                    grid[imp_i+i][imp_j+j] = CRATER
                if(imp_j+j < SIZE and imp_j-j>0):
                    #if(imp_j+j >= SIZE): print SIZE
                    #print "imp_j+j: ", imp_j+j
                    grid[imp_i][imp_j-j] = CRATER
                    grid[imp_i][imp_j+j] = CRATER
                    grid[imp_i+i][imp_j-j] = CRATER
                    grid[imp_i+i][imp_j+j] = CRATER
                        
            if(imp_j+j >= SIZE):
                if(imp_i+i >= SIZE):
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i-i][imp_j-j] = CRATER
                    grid[imp_i][imp_j-j] = CRATER

                if(imp_i-i <= 0):
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i-i][imp_j-j] = CRATER
                    grid[imp_i][imp_j-j] = CRATER

                if((imp_i+i < SIZE) and imp_i-i >0):
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i+i][imp_j] = CRATER
                    grid[imp_i-i][imp_j-j] = CRATER
                    grid[imp_i+i][imp_j-j] = CRATER

            if(imp_j-j <= 0):
                if(imp_i+i >= SIZE):
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i-i][imp_j+j] = CRATER
                    grid[imp_i][imp_j+j] = CRATER

                if(imp_i-i <= 0):
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i-i][imp_j+j] = CRATER
                    grid[imp_i][imp_j+j] = CRATER

                if(imp_i+i < SIZE and imp_i-i>0):
                    #if(imp_i+i >= SIZE): print SIZE
                    #print "imp_i+i: ", imp_i+i
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i+i][imp_j] = CRATER
                    grid[imp_i-i][imp_j+j] = CRATER
                    grid[imp_i+i][imp_j+j] = CRATER     
           
            if(imp_j+j < SIZE and imp_j-j >=0 and imp_i +i < SIZE and imp_i - i >=0):
                grid[imp_i-i][imp_j-j] = CRATER
                grid[imp_i+i][imp_j-j] = CRATER
                grid[imp_i-i][imp_j +j] = CRATER
                grid[imp_i+i][imp_j +j] = CRATER
            #print("imp_i: ", imp_i, " imp_j: ", imp_j)
            #print("imp_i + i: ", imp_i + i, " imp_j+j: ", imp_j+j)

        grid[imp_i][imp_j] = CENTER
    return grid
    

#returns true if there is saturation (ie less that 5% change when time doubles
def checkSat(craters, time):
    if(time==0):
        curAvg = 0.0
        oldAvg = 0.0
    else:
        if((time/2)==0):
            curAvg = craters[time] / time
            oldAvg = 0.0
        else:
            curAvg = craters[time] / time
            oldAvg = craters[time/2] / (time/2)
    if(abs(craters[time] - craters[time/2] ) < craters[time/2]*.05):    
    #if(abs(curAvg-oldAvg) < (curAvg * 0.05)):
        #print "curAvg=", curAvg, " oldAvg=",oldAvg, " cur+old=",curAvg-oldAvg, " cur*1.05=",curAvg*0.05
        # print("craters[time]: ", craters[time], " craters[time/2]: ", craters[time/2], " craters[time/2]*.05: ", craters[time/2]*.05)
        if(craters[time] < 10):
            return False
        else:
            return True
    else:
        return False

while not checkSat(craters, time):
    impact = random.randrange(0,1000)

    if(impact == 129):
        grid = makeImpact(grid)
    craters.append(numCraters(grid))
    if(time % 500 == 0):
        print "Time = ", time, " Number of craters= ", craters[time]
        for x in grid:
            print(' '.join(x))
    time += 1

print "\n------------------------------------------------------------results-----------------------------------------------------------"
for x in grid:
    print(' '.join(x))
print"number of craters: ", numCraters(grid)
print "Time to saturation: ", time


