def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        [0,1,2,5,3,4,3,2,4,2]
        
        i=3

        visit = 5

        return false

        


        if the length is less than 2 and items are the same
        return true
        else:
            set visitor variable to keep track to first item
            loop until found 
            if visitor == item visited:

        """
        '''
        #solution works for certin amoutn of inputs since we're not using any data structures
        if len(nums) == 2 and nums[0] == nums[1]:
            return True
        i = 0
        visitor = 1
        while True:
            if visitor == len(nums):
                return False
                
            if i < len(nums) and i != visitor:
                # print(nums[len(nums)%i])
                if nums[i] == nums[visitor]:
                    print('Indexes: ', i, visitor, "Content: ", nums[i], nums[visitor])
                    return True
                i += 1
            else:
                i = 0
                visitor = visitor + 1
        '''
        #using a set

        visited = set()

        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False

#insert test inputs