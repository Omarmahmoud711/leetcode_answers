class Solution(object):
    def canJump(self, nums):
        dest = len(nums)-1
        i =dest-1

        while i>=0:
            if i+nums[i] >= dest:
                dest = i
            i-=1
        return dest==0
