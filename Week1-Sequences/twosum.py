class Solution(object):
    def twoSum(nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2:
            if nums[0] +nums[1] == target:
                return [0,1]
            else:
                return []
        #To store the first index and difference
        idx1= 0
        diff = 0
        #Look for the first index and its difference
        for i in range(len(nums)):
            if (target-nums[i]) in nums[1+i:]:
                idx1 = i
                diff = target - nums[i]
                break
        #Look for the difference in the list and find its index
        for i in range(len(nums)):
            if nums[i] == diff and i != idx1:
                print('ANSWER:', [idx1,i])
                return[idx1,i]


Solution.twoSum(nums=[1,3,4,2],target=6)