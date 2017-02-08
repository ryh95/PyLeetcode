# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def swap(root):
            tmp = root.right
            root.right = root.left
            root.left = tmp


        if root != None:
            swap(root)
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

if __name__ == '__main__':
    a=TreeNode(4)
    b=TreeNode(2)
    c=TreeNode(7)
    d=TreeNode(1)
    e=TreeNode(3)
    f=TreeNode(6)
    g=TreeNode(9)
    # e=TreeNode(3)
    a.left=b
    a.right=c
    b.left=d
    b.right=e
    c.left=f
    c.right=g

    a=None
    a=  Solution().invertTree(a)

    print('Done')