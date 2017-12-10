class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_max = 0
        start = 0
        end = 0
        substr = {} # Current substring
        
        for i in range(len(s)):
            curr_char = s[i]
            
            if curr_char in substr and substr[curr_char] >= start:
                start = substr[curr_char] + 1
                
            substr[curr_char] = i
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
