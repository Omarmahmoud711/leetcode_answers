class Solution(object):
    def jump(self, nums):
        jumps = 0
        current_max_reach = 0
        last_jump_index = 0

        for i in range(len(nums) - 1):
            current_max_reach = max(current_max_reach, i + nums[i])

            if i == last_jump_index:
                jumps += 1
                last_jump_index = current_max_reach

        return jumps
