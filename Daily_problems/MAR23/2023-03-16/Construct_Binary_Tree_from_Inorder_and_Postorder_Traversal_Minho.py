from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        '''
            What is inorder --> Process all nodes of a tree by recursively processing the left subtree, then processing the root, and finally the right subtree
                --> From LEFT subtree to RIGHT subtree

            What is postorder  --> Process all nodes of a tree by recursively processing all subtrees, then finally processing the root (DFS)
                --> From subtrees (no more left, right) to the TOP


            Key point:
                A. postorder[-1] == top node of binary tree
                B. from inorder[postorder[-1]], if nodes left --> left side of top // right --> right side of top
                C. postorder --> nodes from under to top
                D. inorder --> left to right

            Approach
                A. Start with the last element of the postorder array as the root node.                         DONE
                B. Find the index of the root node in the inorder array.                                        DONE
                C. Divide the inorder array into left and right subtrees based on the index of the root node.   DONE
                D. Divide the postorder array into left and right subtrees based on the number of elements      DONE
                    in the left and right subtrees of the inorder array.
                E. Recursively construct the left and right subtrees.                                           DONE                                          

        '''

        # Base case
        if not inorder:
            return None
        
        # The last element of postorder list is the root
        top_node_val = postorder.pop()
        root = TreeNode(top_node_val)
        
        # Find the position of the root in the inorder list
        inorder_index = inorder.index(top_node_val)
        
        # Recursively build the left and right subtrees
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root
