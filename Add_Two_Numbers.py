# https://leetcode.com/problems/add-two-numbers/
# 3/27/2023

# 2. Add_Two_Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      answer = ListNode()
      pointer = answer
      ten = False
      digit = 0
      l1_temp = l1
      l2_temp = l2
      while (l1_temp != None or l2_temp != None):
        if (l1_temp == None and ten == True):
          digit = 1 + l2_temp.val
          l2_temp = l2_temp.next
        elif (l1_temp == None and ten == False):
          digit = l2_temp.val
          l2_temp = l2_temp.next
        elif (l2_temp == None and ten == True):
          digit = 1 + l1_temp.val
          l1_temp = l1_temp.next
        elif (l2_temp == None and ten == False):
          digit = l1_temp.val
          l1_temp = l1_temp.next
        else:
          digit = l1_temp.val + l2_temp.val
          l1_temp = l1_temp.next
          l2_temp = l2_temp.next

        if (digit > 10):
            ten = True
        else:
            ten = False

        if (pointer == None):
          pointer = ListNode()
        pointer.val = digit % 10
        pointer = pointer.next

      if (ten == True):
        pointer = ListNode(val = 1)
      return answer