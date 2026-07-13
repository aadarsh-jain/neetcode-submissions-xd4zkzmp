class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag = dict()
        for i in range(len(strs)):
            k = ''.join(sorted(strs[i]))

            if k in anag:
                anag[k].append(strs[i])
            else:
                anag.update({k:[strs[i]]})
        
        return list(anag.values())