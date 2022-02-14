"""
class Node
    stores data to be held in linkedList
"""
class Node:
	def __init__(self, dataVal = None):
		self.dataVal = dataVal
		self.nextVal = None

"""
class LinkedList
    stores Nodes
    
    push(val)
        pushes a new node to the head or top of the list
        
    pop()
        removes head Node from list and returns it's dataVal
    
    printStack()
        prints all Nodes in list
        
    rot()
        takes head Node of list and places it at bottom of list
        
    getSize()
        returns number of Nodes in list
        
    deletStack()
        deletes all Nodes in Stack
"""
class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0;
		
	def push(self, val):
		newNode = Node(val)
		newNode.nextVal = self.head
		self.head = newNode
		self.size += 1

	def pop(self):
		result = self.head.dataVal
		self.head = self.head.nextVal
		self.size -= 1
		return result

	def printStack(self):
		counter = self.size - 1;
		current = self.head
		print('stacksize is ' + str(self.size))
		while(current is not None):
			print('ind ' + str(counter) + ": " + str(current.dataVal))
			current = current.nextVal
			counter -= 1
		print('\n')

	def rot(self):
		newBottom = self.head
		current = self.head
		self.head = self.head.nextVal
		
		while(current.nextVal is not None):
			current = current.nextVal

		current.nextVal = newBottom
		newBottom.nextVal = None


	def getSize(self):
		return self.size;

	def deleteStack(self):
		while (self.size > 0):
			pop();
