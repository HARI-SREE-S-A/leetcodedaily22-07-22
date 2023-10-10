class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}
        for i,n in enumerate(strs):
            sortedword = "".join(sorted(list(n)))

            if sortedword in mapp:
                mapp[sortedword].append(n)
            else:
                mapp[sortedword] = [n]
                
        return(list(mapp.values()))
