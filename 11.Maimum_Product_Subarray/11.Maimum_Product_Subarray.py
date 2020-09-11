'''	
	Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
	
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        lx = nums[0]
        ly = nums[0]
        g = nums[0]
        for i in range(1, n):
            temp = lx
            lx = max(max(nums[i], nums[i] * lx), nums[i] * ly)
            ly = min(min(nums[i], nums[i] * ly), nums[i] * temp)
            g = max(g, lx)
        return g  