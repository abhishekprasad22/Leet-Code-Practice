"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
# The following solution is a brut force method with O(n^2) time complexity
"""
class Solution(object):
    
    def majorityElement(self, nums):
       
        if not nums:
            return 0

        maxCount = 0
        index = -1
        for i in range(len(nums)):
            count = 1
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

            if count > maxCount:
                maxCount = count
                index = i

        if maxCount >= float(len(nums)) * 0.5:
            return nums[index]
        
nums = [2,2,3,3,3,3,2]
k = Solution()
h = k.majorityElement(nums)
print(h)
"""

# Moore's Voting algorithm is a better approach for this question.

class Solution(object):
    
    def majorityElement(self, nums):
        candidate  = -1
        votes = 0
        n = len(nums)
        for i in range(n):
            if votes == 0:
               candidate = nums[i]
               votes = 1
            else:
                if nums[i] == candidate:
                   votes += 1
                else:
                   votes -= 1

        count = 0

        for i in range(n):
            if nums[i] == candidate:
                count += 1

        if count > n//2:
            return candidate
        else:
            return -1
        

nums = [2,2,3,3,3,3,2]
k = Solution()
h = k.majorityElement(nums)
print(h)
        
