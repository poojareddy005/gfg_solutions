'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def insertAtEnd(self, head, x):
        if(head==None or head.next==None):
            return Node(x)
        temp=head
        while(temp.next):
            temp=temp.next
        newNode=Node(x)
        temp.next=newNode
        newNode.next=None
        return head
        #code here