class Solution:

    '''
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

[4,1,2]

1: 0
1 : 0
4 : 2
2: 3 



is nums j + 1 > key: yes so add to list at nums1[dict[key]]



    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)  # Initialize result list with -1s
        check = {}  # Dictionary to store the indices of elements in nums2

        # Fill the dictionary with indices of elements in nums2
        for i in range(len(nums2)):
            check[nums2[i]] = i

        # Loop through each element in nums1
        for j in range(len(nums1)):
            # Get the index of nums1[j] in nums2 using the check dictionary
            idx = check[nums1[j]]

            # Look for the next greater element in nums2 starting from idx + 1
            for k in range(idx + 1, len(nums2)):
                if nums2[k] > nums1[j]:
                    ans[j] = nums2[k]  # Update ans with the next greater element
                    break  # Stop once the next greater element is found
        
        return ans

'''
THIS IS MY NEW CODE

'''







        