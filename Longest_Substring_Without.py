# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3/28/2023

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring
# without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      answer = ""
      count = 0
      max_count = 0
      for char in s:
          if char in answer:
            max_count = max(count, max_count)
            pos = answer.rfind(char)
            answer = answer[pos+1:] + char
            count = len(answer)
          else:
             count += 1
             answer += char
      return max(max_count, count)

