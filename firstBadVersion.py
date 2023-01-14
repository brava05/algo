# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    first_bad = 0

    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n
        mid = 0
        while left<right:
            mid = (left+right)//2
            if self.isBadVersion(mid) == False:
                left = mid+1
            else:
                right = mid

        return left

    def isBadVersion(self, number):
        if number < self.first_bad:
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    sol.first_bad = 4
    print(sol.firstBadVersion(5))

