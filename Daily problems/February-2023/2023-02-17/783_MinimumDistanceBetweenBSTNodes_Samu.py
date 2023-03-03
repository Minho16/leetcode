# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# O(n) Space and complexity solution (Runtime: 20 ms (62.4%) | Memory: 13.7MB (33%))
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.v = 1000000
        self.li = []
        def dfs(root):
            if root is None:
                return 1000000
            # print(li)
            self.li = self.li + [root.val]
            if self.v <= 1:
                return self.v
            if root.left and root.val - root.left.val < self.v:
                self.v = root.val - root.left.val
            if root.right and root.right.val - root.val < self.v:
                self.v = root.right.val - root.val
            if root.left and root.right:
                return min(dfs(root.left), dfs(root.right), self.v)
            elif root.left:
                return min(dfs(root.left), self.v)
            else:
                return min(dfs(root.right), self.v)
        v = dfs(root)
        if v == 1:
            return v
        l_sort = sorted(self.li)
        i = 0
        while i + 1 < len(l_sort):
            if l_sort[i+1] -l_sort[i] < v:
                v = l_sort[i+1] -l_sort[i]
            i += 1
        return v
    

s = Solution()
t = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(6, None, None))
r = s.minDiffInBST(t)
print(r, r==1)


t = TreeNode(1, TreeNode(-1000, None, None), TreeNode(12, TreeNode(10, None, None), TreeNode(49, None, None)))
r = s.minDiffInBST(t)
print(r, r==2)

# #[27,null,34,null,58,50,null,44]
t = TreeNode(27, None, TreeNode(34, None, TreeNode(58, TreeNode(50,TreeNode(44, None, None), None))))
r = s.minDiffInBST(t)
print(r, r==6)

#[90,69,null,49,89,null,52]
t = TreeNode(90, TreeNode(69, TreeNode(49, None, TreeNode(52, None, None)), TreeNode(89, None, None)))
r = s.minDiffInBST(t)
print(r, r==1)