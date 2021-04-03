# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = None
        temp = None
        carry = 0

        # While both list exists
        while(l1 is not None or l2 is not None):
            fdata = 0 if l1 is None else l1.data
            sdata = 0 if l2 is None else l2.data
            Sum = carry + fdata + sdata

            # update carry for next calculation
            carry = 1 if Sum >= 10 else 0

            # update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10

            # Create a new node with sum as data
            temp = Node(Sum)
            # if this is the first node then set it as head
            # of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            # Set prev for next insertion
            prev = temp

            # Move first and second pointers to next nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if carry > 0:
                temp.next = Node(carry)


solution = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
ans = solution.addTwoNumbers(l1, l2)
print(ans)
