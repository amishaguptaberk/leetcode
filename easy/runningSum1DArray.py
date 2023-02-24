# problem : https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1
# submission : https://leetcode.com/problems/running-sum-of-1d-array/submissions/903902823/?envType=study-plan&id=level-1
# 02/23/23 

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final = [nums[0]]
        for i in range(1, len(nums)):
            final.append(final[i-1] + nums[i])
        return final