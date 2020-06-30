# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        
        temp = head
        
        while temp!=None:
            temp = temp.next
            count+=1
        
        for i in range(int(count/2)):
            head = head.next
            
        return head