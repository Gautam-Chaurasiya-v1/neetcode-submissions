class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        track = {}
        lastIndex = 0

        for str in strs : 
            temp = "".join(sorted(str))
            if temp not in track:
                track[temp] = lastIndex
                ans.append([str])
                lastIndex += 1
            else:
                ans[track[temp]].append(str)

        return ans

