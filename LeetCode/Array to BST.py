'''
Given a sorted array. Convert it into a Height balanced Binary Search Tree 
(BST).
Height balanced BST means a binary tree in which the depth of the two subtrees 
of every node never differ by more than 1.

Example 1:

Input: nums = {1, 2, 3, 4}
Output: {2, 1, 3, 4}
Explanation: 
The preorder traversal of the following 
BST formed is {2, 1, 3, 4}:
     3
    /  \
   2    4
 /
1
'''

# O(n) runtime, O(logn) space complexity
class Solution:
    def sortedArrayToBST(self, nums):
        def helper(l, r):
            if l > r:
                return None

            m = (l+r) // 2  # // reps int division
            root = nums[m]
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            return root

        return helper(0, len(nums)-1)


ans = Solution()
nums = [1, 2, 3, 4]
print(ans.sortedArrayToBST(nums))
