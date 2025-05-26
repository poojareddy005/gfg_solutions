'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.
class Node:
    def __init__(self, data): 
        self.data = data
		self.next = None
class Solution:
    def insertInMiddle(self, head, x):
        if (head==None):
            return Node(x)
        slow=head
        fast=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        front=slow.next
        newNode=Node(x)
        slow.next=newNode
        newNode.next=front
        return head
        #code here