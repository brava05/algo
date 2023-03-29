from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1map = [0]*26
        s2map = [0]*26
        for i in range(len(s1)):
            s1map[ord(s1[i])-ord("a")] += 1
            s2map[ord(s2[i])-ord("a")] += 1

        count = 0
        for i in range(26):
            if s1map[i] == s2map[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            if count == 26:
                return True
            right = ord(s2[len(s1)+i])-ord("a")
            left = ord(s2[i])-ord("a")

            s2map[right] += 1
            if s2map[right] == s1map[right]:
                count += 1
            elif s2map[right] == s1map[right] + 1:
                count -=1

            s2map[left] -=1
            if s2map[left] == s1map[left]:
                count += 1
            elif s2map[left] == s1map[left] -  1:
                count -=1
            # print(count)
        
        return count == 26

# решение с каунтером
# надо освоить каунтер
# def checkInclusion(self, s1: str, s2: str) -> bool:
# 	cntr, w = Counter(s1), len(s1)   

# 	for i in range(len(s2)):
# 		if s2[i] in cntr: 
# 			cntr[s2[i]] -= 1
# 		if i >= w and s2[i-w] in cntr: 
# 			cntr[s2[i-w]] += 1

# 		if all([cntr[i] == 0 for i in cntr]): # see optimized code below
# 			return True

# 	return False

# def checkInclusion(self, s1: str, s2: str) -> bool:
# 	cntr, w, match = Counter(s1), len(s1), 0     

# 	for i in range(len(s2)):
# 		if s2[i] in cntr:
# 			if not cntr[s2[i]]: match -= 1
# 			cntr[s2[i]] -= 1
# 			if not cntr[s2[i]]: match += 1

# 		if i >= w and s2[i-w] in cntr:
# 			if not cntr[s2[i-w]]: match -= 1
# 			cntr[s2[i-w]] += 1
# 			if not cntr[s2[i-w]]: match += 1

# 		if match == len(cntr):
# 			return True

# 	return False


if __name__ == "__main__":
    s1 = "abv"
    s2 = "eidbaooo"
    sol = Solution()
    
    s = sol.checkInclusion(s1, s2)
    print(s)
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").