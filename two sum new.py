class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] in dict:
                return [dict.get(nums[i]), i]
            else:
                ntf = target - nums[i]
                dict[ntf] = i
        return None
