#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 0:12
# @Author  : chenshiyang
# @Site    : 
# @File    : 437路径总和3.py
# @Software: PyCharm
import queue


class NodeTree(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def create(self, list):
        root = NodeTree(list[0])
        print(root.val)
        if len(list) >= 2:
            root.left = self.create(list[1])

        if len(list) >= 3:
            root.right = self.create(list[2])

        return root

    def pathSum(self, root:NodeTree, sum:int) -> bool:
        if not root:return False

        stack = [(root, [root.val])]
        result = 0
        while stack:
            node, val = stack.pop()
            result += val.count(sum)
            val += [0]

            if node.left:
                arr = [ node.left.val + i for i in val]
                stack.append([node.left, arr])

            if node.right:
                arr = [ node.right.val + i for i in val]
                stack.append((node.right, arr))

        return result

if __name__ == '__main__':
     treeDataList = [10,[5,[3,[3],[-2]],[2,[1]]],[-3,[11]]]
     op = Solution()
     tree = op.create(treeDataList)
     # print(op.hasPathSum(tree, 18))
     print(op.pathSum(tree, 8))