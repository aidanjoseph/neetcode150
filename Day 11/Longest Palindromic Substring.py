class Solution:
   def longestPalindrome(self, s: str) -> str:
       #thoughts
       '''
       Brute Force: just all isPalindrome() on all subsequences of s
       not really efficient thuogh
       Ideas:
       could have a two pointer thing, start at front and back
       and move inwards
       first thing to return true for ispalindrome should be the longest
       as we woud only go more inwards which implies shorter
       '''
       # def isPalindrome(s):
       #     i = 0
       #     j = len(s) - 1
       #     #aba
       #     while i < j:
       #         if s[i] != s[j]:
       #             return False
       #         else:
       #             i += 1
       #             j -= 1
       #     return s
       # i = 0
       # j = len(s) - 1
       # if len(s) == 1:
       #     return s
       # while i < j:
       #     if s[i] == s[j]:
       #         ans = isPalindrome(s[i:j+1])
       #         if ans:
       #             return ans
       #     elif i + 1 < j and s[i + 1] == s[j]:
       #         ans = isPalindrome(s[i+1:j+1])
       #         if ans:
       #             return ans
       #     elif i + 1 < j and s[i] == s[j-1]:
       #         ans = isPalindrome(s[i:j])
       #         if ans:
       #             return ans
       #     else:
       #         i += 1
       #         j -= 1
       # return s[0]
       res = ""
       resLen = 0
       for i in range(len(s)):
           #odd length
           l, r = i, i
           while l >= 0 and r < len(s) and s[l] == s[r]:
               if (r-l+1) > resLen:
                   res = s[l:r+1]
                   resLen = r - l + 1
               l -= 1
               r += 1
           #even length
           l, r = i, i + 1
           while l >= 0 and r < len(s) and s[l] == s[r]:
               if (r - l + 1) > resLen:
                   res = s[l:r+1]
                   resLen = r - l + 1
               l -= 1
               r += 1
       return res


