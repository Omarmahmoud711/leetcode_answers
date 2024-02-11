class Solution(object):
    def isIsomorphic(self, s, t):
        hashmap_s = {}
        hashmap_t = {}

        if len(s) != len(t):
            return False
        else:
            i = 0
            j = 0

            while i < len(s) and j < len(t):
                if (s[i] in hashmap_s and hashmap_s[s[i]] != t[j]) or (t[j] in hashmap_t and hashmap_t[t[j]] != s[i]):
                    return False
                else:
                    hashmap_s[s[i]] = t[j]
                    hashmap_t[t[j]] = s[i]
                    i += 1
                    j += 1

            return True
