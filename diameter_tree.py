# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
''''
 diameter of a binary tree: length of the longest path  within the tree between any two nodes

 length of a path between two nodes is the number of edges between the nodes.

 Just the depth?

 O(n)

'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        

        #get the max height of tree of left sub tree and right sub tree
        def dfs(root):
            nonlocal answer
            
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            #get the biggest length for diamater from self and left + right 
            answer = max(answer, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        
        return answer

        