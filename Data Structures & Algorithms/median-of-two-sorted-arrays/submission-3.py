class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        array = [] 
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                array.append(nums1[i])
                i+= 1

            else:
                array.append(nums2[j])
                j += 1

        while i < len(nums1):
            array.append(nums1[i])
            i += 1

        while j < len(nums2):
            array.append(nums2[j])
            j += 1

        median = 0

        if len(array) % 2 == 0:
            return (array[len(array)//2]+array[len(array)//2 - 1])/2

        return array[len(array)//2]