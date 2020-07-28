#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:18
# @Author  : chenshiyang
# @Site    : 
# @File    : 04.04检查平衡性.py
# @Software: PyCharm

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.flag = True

    def create(self, dataList):
        root = TreeNode(dataList[0])

        if len(dataList) >= 2:
            root.left = self.create(dataList[1])

        if len(dataList) >= 3:
            root.right = self.create(dataList[2])

        return root

    def isBalanced(self, root:TreeNode) -> bool:
        self.dfs(root)
        return self.flag

    def dfs(self, root):
        if not root:return -1

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        print('l----------------------', l)
        print('r----------------------', r)

        print('abs---------', abs(l-r))
        if abs(l-r) > 1:
            self.flag = False


        return max(l,r) + 1


if __name__ == "__main__":
    dataList = [1,[2,[3, [4],[4]],[3]],[2]]
    node = Solution()
    tree = node.create(dataList)
    print(node.isBalanced(tree))