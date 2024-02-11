class Solution(object):

    def rotate(self, nums, k):
        k=k%len(nums)
        nums[0:len(nums)+1] = reversed(nums[0:len(nums)+1])
        nums[0:k]=reversed(nums[0:k])
        nums[k:len(nums)+1]=reversed(nums[k:len(nums)+1])






        