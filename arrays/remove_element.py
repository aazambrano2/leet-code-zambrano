'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Source: https://leetcode.com/problems/remove-element/
'''
def remove_element(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        if val not in nums: return len(nums)
        i = 0
        while i < len(nums):
            
            if nums[i] == val: 
                nums.remove(nums[i])
                #takes in account of iterating array while modifying it.
                i = i - 1
            i = i + 1
            print(nums)
                
        return len(nums)
        


if __name__ == '__main__':
    
    
    print(remove_element([3,2,2,3],3)) #2
    print(remove_element([0,1,2,2,3,0,4,2],2))#5
    