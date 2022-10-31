class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_pointer =  m - 1
        right_pointer = n - 1
        iterator = m + n -1
        while left_pointer >= 0 and right_pointer >= 0:
            if nums1[left_pointer] > nums2[right_pointer]:
                nums1[iterator] = nums1[left_pointer]
                left_pointer -= 1
            else:
                nums1[iterator] = nums2[right_pointer]
                right_pointer -=1
            iterator -= 1
        
        if right_pointer >= 0:
            nums1[ :iterator+1] = nums2[ :right_pointer+1]