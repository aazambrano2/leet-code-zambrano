# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
    """
    :type head: ListNode
    :rtype: int
    """
    if head.next is None:
        if head.val == 0: 
            return 0
        else:
            return 1
    temp = head
    binary_string = ''
    while temp is not None:
        binary_string += str(temp.val)
        temp = temp.next
    
    binary_number = int(binary_string)
    
    #Conversion
    add = 0
    n = 0
    while binary_number != 0:
        add += (binary_number % 10) * (2**n)
        binary_number = binary_number / 10
        n += 1
    return add

#Construct List
# print(getDecimalValue(head))