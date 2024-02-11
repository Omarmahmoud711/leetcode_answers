class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote=sorted(ransomNote)
        magazine=sorted(magazine)
        i=0
        j=0
        while i < len(ransomNote) and j<len(magazine):
            if ransomNote[i] == magazine[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i==len(ransomNote)
        
