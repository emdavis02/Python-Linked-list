#importing to access command line arguments
import sys

#importing other classes
from stack import Node
from stack import LinkedList
from operate import Operations

#instanctiating objects
linkedList = LinkedList()
operations = Operations()

#getting command line argument filename
if(len(sys.argv) > 1):
    fileName = sys.argv[1]
    file1 = open(fileName, 'r')
    Lines = file1.readlines()

    #parsing through lines of file
    for line in Lines:
        #breaking up each line to extract opperation and value
        spaceIndex = line.find(' ')
        if(spaceIndex > 0):
            opp = line[0:spaceIndex]
            spaceIndex += 1
            val = line[spaceIndex:]
            halt = operations.operate(opp, linkedList, val)
            if(halt == -1):
                break

        #if no value is in the line
        else:
            opp = line[0:len(line)-1]
            halt = operations.operate(opp, linkedList)
            if(halt == -1):
                break

    #tidying up
    file1.close()
    print('\nprogram terminated')
    linkedList.printStack()