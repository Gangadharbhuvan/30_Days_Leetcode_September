'''
    Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

   Hide Hint #1  
Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
   Hide Hint #2  
We don't care about duplicates or non-positive integers
   Hide Hint #3  
Remember that O(2n) = O(n)


'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n): 
            if (abs(nums[i]) - 1 < n and nums[abs(nums[i]) - 1] > 0): 
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1] 
        for i in range(n): 
            if (nums[i] > 0): 
                return i + 1
        return n + 1
    
    
    
    
## OPTIMISED/EASY SOLUTION
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums==[]:
            return 1
        s = set(nums)
        for i in range(1,len(nums)+2): #[1]
            if i not in s:
                return i
                break
    
   
