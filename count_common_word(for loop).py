class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
       
        i=0
        j=0
        for i in words1:
        
            if words1.count(i) == words2.count(i) == 1:
                j+=1
                
