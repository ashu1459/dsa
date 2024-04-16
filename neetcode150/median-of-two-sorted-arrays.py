class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # solution-1: using sort, TC-O(nlogn) due to sorting
        # nums1.extend(nums2)
        # nums1.sort()

        # l, r = 0, len(nums1) - 1

        # # while l <= r:
        # mid = (l + r) // 2

        # if (r + 1) % 2 == 0:
        #     return (nums1[mid] + nums1[mid+1]) / 2
        # else:
        #     return nums1[mid]

        # Solution-2: O(logn) without sorting
        # Answer Solution Logic - https://www.youtube.com/watch?v=LPFhl65R7ww
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        
        # recursive call again to always have first array as smallest
        if nums1_len > nums2_len:
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, nums1_len - 1
        total_len = nums1_len + nums2_len

        median_of_both_arrays = (total_len + 1) // 2

        while True:
            mid_nums1 = (l + r) // 2
            mid_nums2 = median_of_both_arrays - (mid_nums1 + 2)

            left_num1 = nums1[mid_nums1] if mid_nums1 >= 0 else float("-infinity")
            right_num1 = nums1[mid_nums1+1] if mid_nums1+1 < nums1_len else float("infinity")
            left_num2 = nums2[mid_nums2] if mid_nums2 >= 0 else float("-infinity")
            right_num2 = nums2[mid_nums2+1] if mid_nums2+1 < nums2_len else float("infinity")

            if left_num1 <= right_num2 and left_num2 <= right_num1:
                # found solution
                if total_len % 2 == 0:
                    # even length
                    left_max =  max(left_num1, left_num2)
                    right_min =  min(right_num1, right_num2)

                    return (left_max + right_min) / 2
                else:
                    # odd length
                    return max(left_num1, left_num2)

            elif left_num1 > right_num2:
                r = mid_nums1 - 1
            else:
                l = mid_nums1 + 1




        