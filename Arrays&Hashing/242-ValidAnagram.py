class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # add an immediate stop condition if they are not the same length
        if len(s) != len(t):
            return False

        listS, listT = sorted(s.lower()), sorted(t.lower())
        return listS == listT


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        # add an immediate stop condition if they are not the same length
        if len(s) != len(t):
            return False

        dictS, dictT = {}, {}

        for i in range(len(s)):
            dictS[s[i]] += 1
            dictT[t[i]] += 1

        return dictS == dictT
