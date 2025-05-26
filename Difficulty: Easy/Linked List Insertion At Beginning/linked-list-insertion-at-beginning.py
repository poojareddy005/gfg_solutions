#User function Template for python3
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    # Function to insert a node at the beginning of the linked list
    def insertAtBegining(self, head, x):
        newNode=Node(x)
        newNode.next=head
        head=newNode
        return head
       
        # Code here