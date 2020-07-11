#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 23:22
# @Author  : chenshiyang
# @Site    : 
# @File    : 112路径总和.py
# @Software: PyCharm
import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def create(self, list):
        '''二叉搜索树插入操作'''
        root = TreeNode(list[0])
        lens = len(list)
        if lens >= 2:
            root.left = self.create(list[1])
        if lens >= 3:
            root.right = self.create(list[2])
        return root

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """后续遍历 求和"""
        if not root: return False

        stack = [root]
        cur = root.left
        res = root.val

        while stack:
            while cur:
                stack.append(cur)
                res += cur.val
                cur = cur.left

            r = None
            flag = True

            while stack and flag:
                cur = stack[-1]
                if cur.right == r:
                    if cur.right == None and cur.left == None and res == sum: return True
                    cur = stack.pop()
                    res -= cur.val
                    r = cur
                else:
                    cur = cur.right
                    flag = False
        return False

    def bfs(self, root:TreeNode, sum:int) -> bool:
        """广度优先"""

        if not root:return False
        que = queue.deque()
        que.append((root, root.val))

        while que:
            node , val = que.pop()
            if not node.left and not node.right and val == sum:return True

            if node.left:
                que.append((node.left, node.left.val + val))

            if node.right:
                que.append((node.right, node.right.val + val))

        return False


if __name__ == "__main__":
    """
    [1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]
    """
    treeDataList = [5,[4,[11,[7],[2]]],[8,[13],[4,[1]]]]
    op = Solution()
    tree = op.create(treeDataList)
    # print(op.hasPathSum(tree, 18))
    print(op.bfs(tree, 18))
