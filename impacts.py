#!/usr/bin/python

import random

SIZE = 50
craterSize = SIZE/10
craters = [0]
time = 0
crater = 0
years = 1
EMPTY = '.'
CENTER = 'C'
CRATER = ' '
DEBRIS = '/'

grid = [[EMPTY for x in xrange(SIZE)] for x in xrange(SIZE)]


def numCraters(grid):
    crater = 0
    for i in range(SIZE-1):
        for j in range(SIZE-1):
            if(grid[i][j] == CENTER):
                crater += 1
    return crater

def makeImpact(grid):
    imp_i = random.randrange(0, SIZE-1)
    imp_j = random.randrange(0, SIZE-1)
    #print("imp_i: ", imp_i, " imp_j: ", imp_j)

    #change the of the debris field
    for i in range(int((craterSize*1.2/2)+1)):
        for j in range(int((craterSize*1.2/2)+1)):
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
                    #if(imp_j+j >= SIZE): print SIZE
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
                    #if(imp_j+j >= SIZE): print SIZE
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
                    #print "i got in"
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS
                    grid[imp_i][imp_j+j] = DEBRIS
                if(imp_i-i <= 0):
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS
                    grid[imp_i][imp_j+j] = DEBRIS
                if(imp_i+i < SIZE and imp_i-i>0):
                    #if(imp_i+i >= SIZE): print SIZE
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
    
    # change area of crater, over writes debris other than at the edges
    for i in range((craterSize/2)+1):
        for j in range((craterSize/2)+1):
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
    if(abs(craters[time] - craters[time/2] ) < craters[time/2]*.05):
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
    if(time % 2000 == 0):
        print "Time = ", time, " Number of craters= ", craters[time]
        for x in grid:
            print x
    time += 1

print "\n--------------------------------------------------------------------------results---------------------------------------------------------------------------------"
for x in grid:
    print x
print"number of craters: ", numCraters(grid)
print "Time to saturation: ", time


