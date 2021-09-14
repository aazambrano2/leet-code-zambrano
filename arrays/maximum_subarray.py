'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Source: https://leetcode.com/problems/maximum-subarray/
'''
def max_subarray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1: return nums[0]
        #Dynamic Programming: Kadane's Algorithm

        #Initialize variables using the first element
        current_subarray = nums[0]
        max_subarray = nums[0]
        #start with the second element sicne we already used the first one
        for i in range(1,len(nums)):
            #if current_subarray is negative, throw it away. Otherwise, keep adding it
            '''
            A clever way to update currentSubarray is using currentSubarray = max(num, currentSubarray + num). 
            If currentSubarray is negative, then num > currentSubarray + num.
            '''
            current_subarray = max(nums[i], current_subarray + nums[i])
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray

if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) #6
    print(max_subarray([1])) #1
    print(max_subarray([5,4,-1,7,8])) #23