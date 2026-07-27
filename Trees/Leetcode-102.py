'''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000'''

from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.l=[]
        self.queue=[root]    
        while self.queue:
            self.level=[]
            for i in range(len(self.queue)):
                temp=self.queue.pop(0)
                # print(temp.val, end=" ")
                self.level.append(temp.val)
                if temp.left:
                    self.queue.append(temp.left)
                if temp.right:
                    self.queue.append(temp.right)
            self.l.append(self.level)
        return self.l



