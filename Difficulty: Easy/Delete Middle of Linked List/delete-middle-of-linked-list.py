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


class Solution:

    def deleteMid(self, head):
        if(head==None or head.next==None):
            return None
        prev=None
        slow=head
        fast=head
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        slow.next=None
        return head
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''

        #code here