class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            if l >r:
                return -1

            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            elif nums[m] > target:
                return binarySearch(l, m - 1)
            
            return binarySearch(m + 1, r)


        return binarySearch(0, len(nums)-1)