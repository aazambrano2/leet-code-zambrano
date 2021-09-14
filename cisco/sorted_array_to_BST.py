# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    #Normal construction of a balanced binary search tree

    if len(nums) == 0:
        return None


    head = TreeNode(nums[len(nums)//2])

    head.left = self.sortedArrayToBST(nums[:len(nums)//2])
    head.right = self.sortedArrayToBST(nums[(len(nums)//2) + 1:])

    return head