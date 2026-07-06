class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}

        for char in s:
            mp[char] = mp.get(char,0) + 1

        for char in t:
            mp[char] = mp.get(char,0) - 1
            if mp.get(char) < 0:
                return False

        for num in mp.values():
            if num > 0:
                return False

        return True
