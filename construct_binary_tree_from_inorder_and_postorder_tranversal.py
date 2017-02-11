# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder) == 1:
            return TreeNode(inorder[0])
        elif len(inorder) == 0:
            return None

        # 取出postorder中的最后一个数
        val = postorder[-1]

        # 找到这个数在inorder中的位置
        # 将原inorder分为左右两部分
        # 左边的是左子树
        # 右边的是右子树
        pos = inorder.index(val)

        # 构造根节点
        root = TreeNode(val)

        #把这个位置传给inorder和postorder列表，用以截断列表
        # 递归
        # 注意：递归的时候要把根节点除去
        root.left = self.buildTree(inorder[:pos],postorder[:pos])
        root.right = self.buildTree(inorder[pos+1:],postorder[pos:-1])

        return root

if __name__ == "__main__":
    root = Solution().buildTree([2,1,3],[2,3,1])

    print("Done")