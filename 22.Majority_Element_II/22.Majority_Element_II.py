'''
	Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
   Hide Hint #1  
How many majority elements could it possibly have?


'''

class Solution:
    def majorityElement(self, nums):
        count = Counter()
        for num in nums:
            count[num] += 1
            if len(count) == 3:
                for elem, freq in count.items(): count[elem] -= 1
                    
        cands = Counter(num for num in nums if num in count)      
        return [num for num in cands if cands[num] > len(nums)/3]