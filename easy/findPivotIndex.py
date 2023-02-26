# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
# 02.26.23 13:58
#

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        for i in range(len(nums) - 1): 
            list1 = nums[:i]
            if i == len(nums) - 1 :
                list2 = [0]
            else:
                list2 = nums[i+1:]
            if sum(list1) == sum(list2): 
                return i
        return -1 
                
#better solution : since the usm of elements to right and left must be equal, that means it is 2 * sum on one side == total - value at pivot index 

class Solution(object):
    def pivotIndex(self, nums):
        total = 0 
        for num in nums:
            total += num
        for i in range(len(nums)): 
            if sum(nums[:i]) * 2 == total - nums[i]: 
                return i 
        return - 1