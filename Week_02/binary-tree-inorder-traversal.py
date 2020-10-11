#coding:utf-8
#2020-10-11 22:22
#非递归实现二叉树的中序遍历

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        tmp_stack = []

        while tmp_stack or root:
            if root:
                tmp_stack.append(root)
                root = root.left
            else:
                tmp = tmp_stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res
