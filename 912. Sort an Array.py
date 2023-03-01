'''
    Below code works but does not comply with time complexity issue :(
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val or self.val == 0:
            if val <= self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


class Solution:
    '''
        Binary tree + DFS --> Time Limit
    
    '''
    
    def __init__(self):
        self.sorted_list = []
    
    def sortArray(self, nums: list) -> list:
        for idx, num in enumerate(nums):
            if idx == 0:
                root = TreeNode(val=num)
            else:
                root.insert(num)
    
        self.check_left_and_input_value(root)
        return self.sorted_list

    def check_left_and_input_value(self, node):
        if node == None:
            return
        else:
            if node.left:
                self.check_left_and_input_value(node.left)
                self.sorted_list.append(node.val)
            elif node.left == None:
                self.sorted_list.append(node.val)
            
            if node.right:
                self.check_left_and_input_value(node.right)


