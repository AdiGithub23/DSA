
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


class Solution:
    def deleteNode(self, node):

        # If this node is the tail, we do nothing: node.next points to None means, it is the tail.
        if node.next is None:
            return

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next


# Print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ") # end=" -> " argument: To print the elements on the same line, separated by arrows
        head = head.next
    print("None")



# Create the linked list from the given values
# 'create_linked_list' function returns the Head of the created linked list 
# Therefore, 'linked_list'  contains the 'head' node of the linked list
linked_list = create_linked_list([4, 5, 1, 9])
print_linked_list(linked_list)

# Find the node to delete (5)
current = linked_list                       # Initialized with the 'head' of the linked list (linked_list)

# current is not None (meaning: we haven't reached the end of the list)
# The value of the current node (current.val) is not equal to 5
while current and current.val != 5:
    current = current.next

# If the node to be deleted wasn't found:
if current is None:
    print("Node with value 5 not found in the linked list")
    exit()

# Call the deleteNode function with the node to delete
solution = Solution()
solution.deleteNode(current)

# Print the modified linked list
print_linked_list(linked_list)
