
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: "ListNode") -> bool:
        list_in_str = str(head.val)
        while head.next is not None:
            list_in_str = list_in_str + str(head.next.val)
            head = head.next

        if list_in_str == list_in_str[::-1]:
            return True
        else:
            return False

# making test linked list
linked_list_str = reversed("12345654321")
pre_node = None
for i in linked_list_str:
    ln = ListNode(int(i), pre_node)
    pre_node = ln
# testing
palindrom_checker = Solution()
print(palindrom_checker.isPalindrome(pre_node))