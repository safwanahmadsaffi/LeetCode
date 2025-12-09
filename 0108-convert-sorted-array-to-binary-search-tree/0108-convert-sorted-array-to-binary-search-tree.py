from typing import List, Optional

# The 'TreeNode' class is assumed to be globally available 
# in the environment where this code is executed.

class Solution:
    """
    Solves the LeetCode 108 problem: Convert Sorted Array to Binary Search Tree.
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted integer array 'nums' to a height-balanced BST 
        using a recursive binary search approach.
        """

        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            """
            Recursive helper function to build the tree from the sub-array 
            defined by indices [left, right] (inclusive).
            """
            # Base case: if the sub-array is empty, return None
            if left > right:
                return None
            
            # Find the middle element to serve as the root of the current sub-tree.
            # Using integer division // 2
            mid = (left + right) // 2
            
            # Create the root node using the platform's provided TreeNode class
            root = TreeNode(nums[mid]) 
            
            # Recursively build the left sub-tree using the left half of the array
            root.left = build_tree(left, mid - 1)
            
            # Recursively build the right sub-tree using the right half of the array
            root.right = build_tree(mid + 1, right)
            
            return root
        
        # Start the process by building the tree from the entire array range [0, len(nums) - 1]
        return build_tree(0, len(nums) - 1)

# Example Usage (for local testing, requires a local TreeNode definition):
# If testing locally, you need to uncomment the following definition:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# nums1 = [-10, -3, 0, 5, 9]
# solution = Solution()
# root1 = solution.sortedArrayToBST(nums1)
# print(root1.val) # Expected: 0
