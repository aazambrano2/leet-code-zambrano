'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Source: https://leetcode.com/problems/search-insert-position/
'''
def search_insert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        if target < nums[0]: return 0
        
        if len(nums) == 1:
            if target == nums[0]: return 0
            if target < nums[0]: return 0
            else: return 1
        for i in range(len(nums)):
            #1st case: target is found
            if nums[i] == target:
                    return i
        #2nd case: target not found
        for j in range(len(nums)):
                if target < nums[j]:
                        return j 
        #target was not found and is greater than every element
        return len(nums) 


                
                

if __name__ == '__main__':
    print(search_insert([1,3,5,6], 5))#2
    print(search_insert([1,3,5,6], 2))#1
    print(search_insert([1,3,5,6], 7))#4
    print(search_insert([1,3,5,6], 0))#0
    print(search_insert([1], 0))#0