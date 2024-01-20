# Tc- only one loop so O(n)
# sc-3O(n)
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_array=[]
        new_array.extend(nums1)
        new_array.extend(nums2)
        sum=0
        for i in new_array:
            sum=sum+i
        result=float(sum/len(new_array))
        return result 