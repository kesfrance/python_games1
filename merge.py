#!/usr/bin/python3
#
# merge.py: A helper function in the 2048 game
#
# by: Francis Kessie
# 
# I am developing a clone for Gabriele Cirulli's popular game "2048". 
# This is the first phase of the project and involves developing the 
# merge function. 

"""
This function merges rows in a column when playing the game
"""
# the original game can be found at http://gabrielecirulli.github.io/2048
#
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # create a list of non zero values from input
    input_size = len(line)
    line = [dummy_value for dummy_value in line if dummy_value > 0]
   
    # create an output list of same length as input with zero values
    line2 = [0] * input_size
    
    #update the output list with the non zero input list based on certain conditions
    line2[0:len(line)] = line
    
    pos = [dummy_no for dummy_no in range(0, len(line2))]
    
    for jos in pos[0:input_size -1]:
        if line2[jos] == line2[pos[jos+1]]:
           line2[jos] = line2[jos] + line2[pos[jos+1]]
           line2[jos+1] = 0
   
    # repeat last two steps above
    # create an output list of same length as input with zero values
    line2 = [dummy_val for dummy_val in line2 if dummy_val > 0]
    
    # create an output list of same length as input with zero values
    line3 = [0] * input_size
    
    #update the output list with the non zero input list 
    line3[0:len(line2)] = line2
    
    return line3

if __name__== "__main__":
    print(merge([2,2,4]))
    print(merge([8,16,16,8]))
    print(merge([2,8,16,16,8,8,2]))
