#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteHead(head):
    front=head.next
    head.next=None
    return front
    #code here
   