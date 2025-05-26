#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
	    self.next = None
class Solution:
    def constructLL(self, arr):
        head=None
        for data in arr:
            if head==None:
                head=Node(data)
                temp=head
            else:
                temp.next=Node(data)
                temp=temp.next
        return head
        # code here