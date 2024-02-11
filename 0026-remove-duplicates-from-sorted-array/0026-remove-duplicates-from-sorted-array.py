class Solution(object):
    def removeDuplicates(self, nums):
        i=j=k=0
        while i<len(nums) and j<len(nums):
            if nums[j]==nums[i]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                k+=1
        return k+1   