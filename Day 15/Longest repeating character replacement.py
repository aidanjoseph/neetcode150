class Solution:
   def characterReplacement(self, s: str, k: int) -> int:
       #thoughts
       '''
       n^2 type solution
       for each character proceed to right in array
       that character is the repeating one we want
       and we continue until we find >k diff characters
       this approach does not work!
       consider BAAAB, and k = 2
       optimal is replace b's with A but my thing only finds BAAAA
       prob have to go with a contains duplicates approach but so
       lets populate with a hashmap instead
       '''


       freqs = defaultdict(int)
        res = 0
        i = 0


        for j in range(len(s)):
            freqs[s[j]] += 1
            maxFreq = max(freqs.values())
            curLen = j - i + 1
            if curLen - maxFreq > k:
                freqs[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        
        return res


