#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:08:45 2017

@author: shahensha

This solutions runs in O(n). It is slightly harder to see at first. But notice
that each number is added to the deque once and removed once. A number if removed 
in two ways:
    1. After the windows moves to the right, the leftmost is popped.
    2. If the new number is greater than the numbers to its left, they are removed.
    
Thus, it can be noticed that comparisons are made only for removal. Thus even
comparisons are linear in terms of n. Every addition, removal and comparison takes
O(1) time and happen constant number of times for every n. Thus making the entire
running time O(n).
"""

from collections import deque

class MaxWindow(object):
    
    def __init__(self, window_size):
        self.k = window_size
        self.max_window = deque()
        self.counter = 0


    def update(self, new_num):
        #print self.counter, new_num, self.max_window, 
        if self.max_window and (self.max_window[0][1] - self.counter) <= -self.k:
            #print "Calling pop left",
            self.max_window.popleft()
        while self.max_window and self.max_window[-1][0] <= new_num:
            self.max_window.pop()
        self.max_window.append((new_num, self.counter))
        self.counter += 1
        #print self.max_window
        return self.max_window[0][0]
    

class Solution(object):
    
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mw = MaxWindow(k)
        result = []
        for num in nums:
            result.append(mw.update(num))
        return result[k-1:]
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7, 1, 2, 3]
    nums2 = [1,3,-1,-3,5,3,6,7]
    print s.maxSlidingWindow(nums, 3)
    print s.maxSlidingWindow(nums2, 3)