class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        left=self.isBalanced(root.left)
        right=self.isBalanced(root.right)
        if abs(self.depth(root.left)-self.depth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def depth(self,root)->bool:
        if root==None:
            return 0
        return max(1+self.depth(root.left),1+self.depth(root.right))