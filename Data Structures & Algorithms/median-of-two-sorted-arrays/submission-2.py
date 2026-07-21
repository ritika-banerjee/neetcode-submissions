class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        array = [] 
        i = 0
        j = 0
        k = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                array.append(nums1[i])
                i+= 1

            elif nums1[i] > nums2[j]:
                array.append(nums2[j])
                j += 1

            else:
                array.append(nums1[i])
                array.append(nums2[j])
                i+=1
                j+=1

        while i < len(nums1):
            array.append(nums1[i])
            i += 1

        while j < len(nums2):
            array.append(nums2[j])
            j += 1

        print(array)
        start = 0
        end = len(array) - 1
        mid = (start + end)//2

        print(mid)
        median = 0
        if len(array) % 2 == 0:
            median = (array[mid] + array[mid+1])/2
            print("even")
        else:
            print("odd")
            median = array[mid]

        return median