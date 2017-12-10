class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_max = 0
        start = 0
        end = 0

        for i in range(len(s)):
            curr_char = s[i]
            
            match_index = -1
            for j in range(start, end):
                if curr_char == s[j]:
                    match_index = j

            if match_index >= 0:
                start = match_index + 1

            end += 1
            curr_max = max(curr_max, end - start)
            #print s[start:end]
        return curr_max

if __name__ == "__main__":
    s = Solution()
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "water"]
    # test_cases = ["abcabcbb"]
    for test_case in test_cases:
        print s.lengthOfLongestSubstring(test_case)
