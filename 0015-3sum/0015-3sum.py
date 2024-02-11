class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            target = nums[i] * -1
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return triplets
