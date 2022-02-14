#importing classes
from stack import Node
from stack import LinkedList

"""
class Operations
    operater(self, opp, linkedList, val = None)
        locates which opperation is being used, and actualizes said opperation
        val is only needed if opp is an operation that requires a val (such as push())
"""
class Operations:
    #going through each option and performing operation
    def operate(self, opp, linkedList, val = None):
        
        if(opp.upper() == 'PUSH'):
            if(val is not None):
                linkedList.push(val)
                return 
            
            return -1
        
        if(opp.upper() == 'POP'):
            if(linkedList.getSize() > 0):
                return linkedList.pop()

            return -1
            
        if(opp.upper() == 'SWAP'):
            if(linkedList.getSize()>= 2):
                node1 = linkedList.pop()
                node2 = linkedList.pop()
                
                linkedList.push(node1)
                linkedList.push(node2)
                return
            
            return -1
            
        if(opp.upper() == 'ROT'):
            if(linkedList.getSize()>= 2):
                linkedList.rot()
                return
            
            return -1
            
        if(opp.upper() == 'DUP'):
            if(linkedList.getSize()>= 1):
                node1 = linkedList.pop()
                linkedList.push(node1)
                linkedList.push(node1)
                return
            
            return -1
            
        if(opp.upper() == 'GET'):
            val = input("Enter your value: ")
            linkedList.push(val)
            return
            
        if(opp.upper() == 'PRINT'):
            if(linkedList.getSize()>= 1):
                node1 = linkedList.pop()
                print(node1)
                linkedList.push(node1)
                return
            
            return -1
        

        if(opp.upper() == 'PRINTSTACK'):
            if(linkedList.getSize()>= 1):
                linkedList.printStack()
                return
            
            return -1
            
        if(opp.upper() == 'CMPI'):
            if(linkedList.getSize()>= 1):
                node1 = linkedList.pop()
                
                if(val != None and node1 == val):
                    linkedList.push(node1)
                    linkedList.push(1)
                else:
                    linkedList.push(node1)
                    linkedList.push(0)
                return
            
            return -1 
            
        if(opp.upper() == 'HALT'):
            return - 1
            
        if(opp.upper() == 'ADD'):
            if(linkedList.getSize()>= 2):
                node1 = int(linkedList.pop())
                node2 = int(linkedList.pop())
                
                sum = node1 + node2
                linkedList.push(sum)
                return
            
            return -1
            
        if(opp.upper() == 'SUB'):
            if(linkedList.getSize()>= 2):
                node1 = int(linkedList.pop())
                node2 = int(linkedList.pop())
                
                sum = node1 - node2
                linkedList.push(sum)
                return
            
            return -1
            
        if(opp.upper() == 'MULT'):
            if(linkedList.getSize()>= 2):
                node1 = int(linkedList.pop())
                node2 = int(linkedList.pop())
                
                sum = node1 * node2
                linkedList.push(sum)
                return
            
            return -1
            
        if(opp.upper() == 'NOT'):
            if(linkedList.getSize() >= 1):
                node1 = linkedList.pop()
                if(node1 == 0):
                    linkedList.push(1)
                else:
                    linkedList.push(0)
                return
            
            return -1
        
        #default case
        return -1
            
        