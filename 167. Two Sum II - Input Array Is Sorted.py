class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        used = []
        for i in range(len(numbers)):
            need = target - numbers[i]
            if need in used:
                return [used.index(need)+1, i+1]
            else:
                used.append(numbers[i])
    
    def twoSumSorted(self, numbers: list[int], target: int) -> list[int]:
        l,r=0,len(numbers)-1
        while(l<r):
            sum=numbers[l]+numbers[r]
            if(sum==target):return [l+1,r+1]
            elif sum>target:r-=1
            else:l+=1


if __name__ == "__main__":
    nums = [2,3,4]
    target = 6
    sol = Solution()
    
    print(sol.twoSum(nums, target))
    # Output: [1,3]