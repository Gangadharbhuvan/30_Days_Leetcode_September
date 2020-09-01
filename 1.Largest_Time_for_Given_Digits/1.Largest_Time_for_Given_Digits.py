'''
    Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9

'''

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def to_minute(arr):
            hour = 10 * arr[0] + arr[1]
            minute = 10 * arr[2] + arr[3]
            if hour < 24 and minute < 60: # valid time
                return hour * 60 + minute
            else:
                return -1
            
        def backtracking(i):
            if i == len(A): # finished one permutation
                self.res = max(self.res, to_minute(A))
            else:
                for j in range(i, len(A)):
                    A[i], A[j] = A[j], A[i]
                    backtracking(i + 1)
                    A[i], A[j] = A[j], A[i]
        
        def to_time(minute):
            if minute == -1: return ""
            hour_s = minute // 60
            min_s = minute % 60
            return '%02d:%02d' % (hour_s, min_s)
        
        self.res = -1
        backtracking(0)
        return to_time(self.res)