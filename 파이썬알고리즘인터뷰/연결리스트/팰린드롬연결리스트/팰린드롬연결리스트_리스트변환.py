

"""
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false


Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9



"""



from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1. 리스트변환
def isPalindrome(head: Optional[ListNode]) -> bool:
    q: List = []

    if not head:
        return True

    
    node = head
    
    # 리스트 변환

    while node is not None:
        q.append(node.val)







print(isPalindrome([1,2,2,1]))
print(isPalindrome([1,2]))



