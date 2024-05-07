from typing import Optional



# Represents a single node within the linked list structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create a linked list from a list of values
def create_linked_list(values):
    head = None                 # to keep track of the first node in the linked list
    tail = None                 # to keep track of the last node in the linked list
    for val in values:
        new_node = ListNode(val)    # a new ListNode object is created for each value in values
        if head is None:
            head = new_node     # creating the first node in the linked list 
        else:
            tail.next = new_node    # set the 'next' pointer of the current tail node to point to the 'new_node'
        tail = new_node             # update the 'tail' to point to the 'new_node'
    return head

#region METHOD 01: WORKS FINE, BUT EXCEEDS TIME 

# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Handle empty list
#         if not head or not head.next:
#             return head
        
#         current = head
#         prev = None

#         while current:
#             # Check if a greater value exists to the right
#             greater_found = False
#             runner = current.next
#             while runner:
#                 if runner.val > current.val:
#                     greater_found = True
#                     break
#                 runner = runner.next

#             # If no greater value found, keep the node
#             if not greater_found:
#                 if not prev:
#                     head = current  # Update head if necessary
#                 else:
#                     prev.next = current
#                 prev = current
#             current = current.next

#         # Handle the last node (prev might not be updated)
#         if prev:
#             prev.next = None

#         return head
#endregion

# METHOD 02: USING STACKS
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        stack = []                  # Initializes an empty stack
        current = head              # Sets a pointer 'current' to the head of the linked list for traversal

        while current:
        # Check if stack is empty or current value is greater than top value
            while stack and stack[-1].val < current.val:
                stack.pop()  # Remove smaller values from the stack
            stack.append(current)  # Push current node onto the stack
            current = current.next

        # Rebuilding List with Dummy Node
        temp = ListNode(0)
        prev = temp
        
        for node in stack:
            prev.next = node
            prev = prev.next
        
        prev.next = None        
        return temp.next


# Print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ") # end=" -> " argument: To print the elements on the same line, separated by arrows
        head = head.next
    print("None")



linked_list = create_linked_list([5,2,13,3,8])
print_linked_list(linked_list)

current = linked_list                       # Initialized with the 'head' of the linked list (linked_list)

solution = Solution()
modified_linked_list = solution.removeNodes(current)

# Print the modified linked list
print_linked_list(modified_linked_list)
