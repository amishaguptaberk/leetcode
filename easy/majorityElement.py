# https://leetcode.com/problems/majority-element/description/
# https://leetcode.com/problems/majority-element/solutions/
# 02/23/23 19:51
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_dict = {}

        for num in nums: 
            count = 0
            if majority_dict.has_key(num) : 
                majority_dict[num]+= 1
            else: 
                majority_dict[num] = 1
        for key in majority_dict.keys(): 
            if majority_dict[key] > len(nums)/2:
                return key 
# Boyer algorithm 
    def majorityElement(self, nums):
        candidate = 0
        count = 0
        for num in nums: 
            if count == 0 : 
                candidate = num
            count = (1 if candidate == num else -1)