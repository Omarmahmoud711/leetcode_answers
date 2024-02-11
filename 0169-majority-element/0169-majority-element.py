class Solution(object):
    def majorityElement(self, nums):
        major_appearance = len(nums)/2 +1
        ##
        nums.sort()
        #o(n)
        j=0
        i=0
        count=0
        while j < len (nums):
            if nums[i]==nums[j]:
                j+=1
                count+=1
                if count==major_appearance:
                    break
            else:
                i=j
        return nums[i]

