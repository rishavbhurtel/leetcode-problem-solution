# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for x in range(0,len(nums)):
#             for y in range(0,len(nums)):
#                 if nums[x] + nums[y] == target and x != y:
#                     return [x, y]
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = { i : nums[i] for i in range(0, len(nums) ) }
        for x in range(0,len(nums)):
            y = target - dct[x]
            for key, value in dct.items():
                if value == y and x != key:
                    return [x,key]
