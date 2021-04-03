'''
Given a sorted array nums, remove the duplicates in-place such 
that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do 
this by modifying the input array in-place with O(1) 
extra memory.

Note: Output is different comapred to the description of the problem.  It is expected to return an int but on leet code
it expects an array.
'''
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return 1

        #usually a set would be ideal solution,but the space complexity must be O(1)
        '''
        a = set()

        for n in nums:
            a.add(n)
        '''

        #using the slow runner fast runner technique
        slow_runner = 0
        for fast_runner in range(1,len(nums)):
            if nums[fast_runner] != nums[slow_runner]:
                #increment and update slow runner
                slow_runner = slow_runner + 1
                nums[slow_runner] = nums[fast_runner] 
        return slow_runner + 1


if __name__ == "__main__":
    print(removeDuplicates([1,1,2]))
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


    

    