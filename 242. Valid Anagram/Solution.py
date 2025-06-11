class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}

        for sc in s:
            s_set[sc] = s_set.get(sc,0) + 1

        if not len(s) == len(t):
            return False

        for tc in t:
            if tc not in s_set:
                return False
            elif s_set[tc] < 1:
                return False
            else:
                s_set[tc] = s_set.get(tc, 0) - 1
        
        return True