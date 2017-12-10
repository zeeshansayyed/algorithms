class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = (len(nums1) + len(nums2)) / 2
        n = len(nums1) + len(nums2)

        if len(nums1) <= len(nums2):
            shortA = nums1
            longA = nums2
        else:
            shortA = nums2
            longA = nums1

        ks_floor, kl_floor = -1, -1 # Define lower limits
        ks_ceil, kl_ceil = len(shortA) - 1, len(longA) - 1 # Define upper limits
        ks = min(len(shortA) - 1, k / 2) # Initial k estimate for short
        kl = k - ks - 1 # Initial k estimate for long array
            
        found_median = False
        
        while not found_median:
            if ks < 0 or kl < 0:
                found_median = True
            else:
                if shortA[ks] < longA[kl]:
                    if ks < len(shortA) - 1 and shortA[ks + 1] < longA[kl]:
                        ks_floor = ks
                        ks = max((ks + ks_ceil)/2, ks + 1)
                        kl = k - ks - 1
                    else:
                        found_median = True
                else:
                    if kl < len(longA) - 1 and longA[kl + 1] < shortA[ks]:
                        ks_ceil = ks
                        ks = min((ks + ks_floor)/2, ks - 1)
                        kl = k - ks -1
                    else:
                        found_median = True
                        
            print k, ks, kl, shortA[ks], longA[kl]
            
        if n % 2 == 0:
            if ks == -1:
                val1 = longA[kl]
                val2 = longA[kl-1]
            elif ks == 0 and kl == 0:
                val1 = shortA[ks]
                val2 = longA[kl]
            elif ks == 0:
                val1 = longA[kl]
                if shortA[ks] > longA[kl-1]:
                    val2 = shortA[ks]
                else:
                    val2 = longA[kl-1]
            elif kl == 0:
                val1 = shortA[ks]
                if longA[kl] > shortA[ks-1]:
                    val2 = longA[kl]
                else:
                    val2 = shortA[ks-1]
            else:
                val1 = shortA[ks]
                val2 = longA[kl]
                if val1 > val2 and shortA[ks-1] > val2:
                    val2 = shortA[ks-1]
                if val2 > val1 and longA[kl-1] > val1:
                    val1 = longA[kl-1]
            median = (val1 + val2) / 2.0
        else:
            if ks == -1:
                median = longA[kl]
            else:
                median = max(shortA[ks], longA[kl])
                
        return median

if __name__ == "__main__":
    s = Solution()
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "water"]
    test_cases = [([2, 3, 5, 7, 11, 13, 17, 19], [])]
    n1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    n2 = [4, 8, 12, 16, 20, 24, 28, 32]
