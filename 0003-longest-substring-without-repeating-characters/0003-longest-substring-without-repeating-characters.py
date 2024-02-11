class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # A B C A B C A B C
        #   |
        #   L   |
        #       R
        #and so on....

        #SET=(B,C,A)

        
        l=0
        r=0
        max_length=0
        Set=set()

        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1
            Set.add(s[r])
            max_length=max(max_length,r-l+1) #3
        return max_length

