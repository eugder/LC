
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: "ListNode") -> "ListNode":
        node_list = []
        current_node = head
        while current_node.next is not None:
            node_list.append(current_node)
            current_node = current_node.next
        else:
            node_list.append(current_node) # add last node

        mid = len(node_list)//2

        return node_list[mid]

# making test linked list (from end to start)
linked_list_str = reversed("12345")
pre_node = None
for i in linked_list_str:
    ln = ListNode(i, pre_node)
    pre_node = ln
# testing
checker = Solution()
mid_node = checker.middleNode(pre_node)
print("mid node ", mid_node.val)