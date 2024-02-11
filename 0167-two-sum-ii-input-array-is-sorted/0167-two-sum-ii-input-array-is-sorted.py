class Solution(object):
    def twoSum(self, numbers, target):
        #we can solve this as the original two sum , but he needs o(1) in space , so we can't   use a hashmap as this is extra space , instead we are going to use l,r pointers 
        l=0
        r=len(numbers)-1

        while l<r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else :
                return [l+1,r+1]

