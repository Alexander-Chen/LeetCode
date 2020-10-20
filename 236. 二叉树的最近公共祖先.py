class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        if root==p:
            return p
        if root==q:
            return q
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left==None and right==None:
            return None
        elif left==p and right==q:
            return root
        elif left==q and right==p:
            return root
        elif left==p or left==q and right==None:
            return left
        elif right==p or right==q and left==None:
            return right
        elif left and left!=p and left!=q and not right:
            return left
        elif right and right!=p and right!=q and not left:
            return right