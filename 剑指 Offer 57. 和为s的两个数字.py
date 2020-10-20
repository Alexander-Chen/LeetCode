class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        while left!=right:
            if nums[left]+nums[right]==target:
                return [nums[left],nums[right]]
            elif nums[left]+nums[right]<target:
                left=left+1
            elif nums[left]+nums[right]>target:
                right=right-1
