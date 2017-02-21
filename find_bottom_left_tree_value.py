# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.nodes = []
        self.f(root,0)
        max_depth = max([node[1] for node in self.nodes])
        for node in self.nodes:
            if node[1] == max_depth:
                return node[0]

    def f(self,root,d):
        if root!=None:
            self.f(root.left,d+1)
            self.f(root.right,d+1)
            self.nodes.append(((root.val,d)))

if __name__ == "__main__":
    # a=TreeNode(3)
    # b=TreeNode(4)
    # c=TreeNode(7)
    # d=TreeNode(2)
    # e=TreeNode(1)
    # f=TreeNode(5)
    #
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.left = f




    print(Solution().findBottomLeftValue(a))