class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        if len(nums3) % 2 != 0:
            sum_num = 0
            for i in range(0, len(nums3)):
                sum_num = sum_num + i
            array_no = sum_num/len(nums3)
            median = nums3[int(array_no)]
            return median
        else:
            sum_num=0
            for i in range(0,len(nums3)):
                sum_num = sum_num + i
            array_no = sum_num/len(nums3)
            median = (nums3[int(array_no)] + nums3[int(array_no+1)])/2
            return median
                
