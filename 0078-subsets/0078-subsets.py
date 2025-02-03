class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # first count number of subsets
        # then make a list and run a loop till no of subsets
        # then make another list inside loop and run a loop n-1 times of 0 0 0 or 0 0 0 0 in binary then 
        # then inside second loop just check if numers ex 3  & 1<<i times is set if so then get that index and push into the list loop one
        # and after that loop puch 2nd list to list one and just continue


        n = len(nums)
        total_subsets = 1 << n  # Calculate the total number of subsets
        result = []  # Initialize the result list
        
        for mask in range(total_subsets):
            current_subset = []  # List to hold the current subset
            
            for i in range(n):
                # Check if the ith bit is set in the current mask
                if mask & (1 << i):
                    current_subset.append(nums[i])
            
            result.append(current_subset)
        
        return result