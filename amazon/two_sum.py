'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Source: https://leetcode.com/problems/two-sum/
'''
from datetime import date
#Time O(n) Space O(n)
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = dict()
    
    for i,num in enumerate(nums):
        if target - num in nums_dict:
            return [i,nums_dict[target-num]]
        nums_dict[num] = i




        
    

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))

x = 2
y = 3

print("CURRENT NETWORK: ", x,"COUNT: ", y)
    
n = 'milf'
print(n in 'milf1512412341.apd.com')

s = set()

for i in range(10):
    s.add(i)

print(s)
            
    





