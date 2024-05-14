def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if (p and not q) or (not p and q) or (p.left and not q.left) or (p.right and not q.right) or (not p.left and q.left) or (not p.right and q.right) or p.val != q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)