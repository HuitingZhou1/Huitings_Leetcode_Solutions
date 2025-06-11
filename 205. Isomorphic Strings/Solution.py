class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_set = {}
        ts_set = {}

        for st, ts in zip(s,t):
            if st in st_set:
                if st_set[st] != ts:
                    return False
            else:
                st_set[st] = ts

            if ts in ts_set:
                if ts_set[ts] != st:
                    return False
            else:
                ts_set[ts] = st
        
        return True
