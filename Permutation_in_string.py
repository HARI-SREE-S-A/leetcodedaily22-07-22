class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = 1
        while l < r and r < len(s2)+1:

    #print("yes",l,r,s2[l],s2[r])
            if (s1[0]==s2[l] or s1[1]==s2[l]):
                if (s1[0]==s2[r] or s1[1]==s2[r]):
                    return True
          


            l = l+1
            r =r+1
        return False
