#!/usr/bin/python

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import random

# area is 500km x 500 km but is broken into a 10km grid
# therefore we can use a 50 x 50 area and have craters be 5 units large rather than 50
SIZE = 50
craterSize = SIZE/10
craters = [0]
time = 0
crater = 0.0
EMPTY = '-'
CENTER = 'O'
CRATER = ' '
DEBRIS = 'x'

# initialize empty, uncratered grid
grid = [[EMPTY for x in xrange(SIZE)] for x in xrange(SIZE)]

# function that goes through the grid and counts the number of crater centers
def numCraters(grid):
    crater = 0
    for i in range(SIZE-1):
        for j in range(SIZE-1):
            if(grid[i][j] == CENTER):
                crater += 1.0
    return crater

# Randomly pick a spot on the grid and make a crater centering at this location. 
def makeImpact(grid):
    imp_i = random.randrange(0, SIZE-1)
    imp_j = random.randrange(0, SIZE-1)    

    for i in range((craterSize/2)+2):
        for j in range(((craterSize/2)+2)-i/2):
            # must ensure that you won't write outside of the grid, if the center is near an edge of the grid
            
            # create circle of debris first, as this is the largest circle
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
                    grid[imp_i-i][imp_j] = DEBRIS
                    grid[imp_i+i][imp_j] = DEBRIS
                    grid[imp_i-i][imp_j+j] = DEBRIS
                    grid[imp_i+i][imp_j+j] = DEBRIS     
           
            if(imp_j+j < SIZE and imp_j-j >=0 and imp_i +i < SIZE and imp_i - i >=0):
                grid[imp_i-i][imp_j-j] = DEBRIS
                grid[imp_i+i][imp_j-j] = DEBRIS
                grid[imp_i-i][imp_j +j] = DEBRIS
                grid[imp_i+i][imp_j +j] = DEBRIS

    # make a smaller circle within the debris circle for the actual crater
    for i in range((craterSize/2)+1):
        for j in range(((craterSize/2)+1)-i/2):
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
                    grid[imp_i-i][imp_j] = CRATER
                    grid[imp_i+i][imp_j] = CRATER
                    grid[imp_i-i][imp_j+j] = CRATER
                    grid[imp_i+i][imp_j+j] = CRATER     
           
            if(imp_j+j < SIZE and imp_j-j >=0 and imp_i +i < SIZE and imp_i - i >=0):
                grid[imp_i-i][imp_j-j] = CRATER
                grid[imp_i+i][imp_j-j] = CRATER
                grid[imp_i-i][imp_j +j] = CRATER
                grid[imp_i+i][imp_j +j] = CRATER           

        grid[imp_i][imp_j] = CENTER   #finally place the center at the center of the impact
    return grid
    

#returns true if there is saturation (ie less that 5% change when time doubles)
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
    if(abs(craters[time] - craters[time/2]) < craters[time/2]*0.05):    
    #if(abs(curAvg-oldAvg) < (curAvg * 0.05)):
        #print "curAvg=", curAvg, " oldAvg=",oldAvg, " cur+old=",curAvg-oldAvg, " cur*1.05=",curAvg*0.05
        # print("craters[time]: ", craters[time], " craters[time/2]: ", craters[time/2], " craters[time/2]*.05: ", craters[time/2]*.05)
        if(craters[time] < 5):
            return False
        else:
            return True
    else:
        return False

# while the grid is not saturated with craters continue randomly generating impacts and increasing time
while not checkSat(craters, time):
    # cratering rate is 1 impact every 1000 years, therefore every year chance of impact is 1/1000
    # generate a number between 1 and 1000
    impact = random.randrange(1,1000)

    # if the random number is some specific number make an impact
    if(impact == 129):
        grid = makeImpact(grid)
    craters.append(numCraters(grid))
    if(time % 30000 == 0):
        print "\nTime = ", time, " Number of Craters= ", craters[time]
        for x in grid:
            print(' '.join(x))
    time += 1

print "\n------------------------------------------------------------results-----------------------------------------------------------"
for x in grid:
    print(' '.join(x))
print "Number of Craters: ", numCraters(grid)
print "Years to Saturation: ", time
print "Time  |  Number of Craters"
for i in range(len(craters)):
   if(i % 10000 == 0):
        toprint = ""
        for x in range(int(craters[i])):
            toprint += "*"
        print i, " | ", toprint, " ", craters[i]
