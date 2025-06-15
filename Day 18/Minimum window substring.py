class Solution:
   def minWindow(self, s: str, t: str) -> str:
       #thoughts
       '''
       uh is this a hard or am i tripping
       can't i just having a sliding window
       start from a, and extend until i find the rest
       consider ex 1, i find A then i continue until if find both b and c
       so ADOBEC, and then thats my curr min, then i continue from char B
       worst case n^2 i think cuz theoericalty
       something like AAAAAAAAAAAAAAAAABC, would start at every single A
       but i mean its an idea
       #checking if we have all the chars in t is a lot more annoying than i thought
       #i mean we could do a remove type operation
       #we have a set(t) and for each char if its in t then we remove it
       and if the set is empty then we right, but we need position of first
       so a hashmap
       '''
       if len(s) < len(t):
           return ""
       char_count = defaultdict(int)
       for char in t:
           char_count[char] += 1
       target_chars_remaining = len(t)
       min_window = (0, float("inf"))
       start_index = 0
       for end_index, char in enumerate(s):
           if char_count[char] > 0:
               target_chars_remaining -= 1
           char_count[char] -= 1
           if target_chars_remaining == 0:
               while True:
                   char_at_start = s[start_index]
                   if char_count[char_at_start] == 0:
                       break
                   char_count[char_at_start] += 1
                   start_index += 1
               if end_index - start_index < min_window[1] - min_window[0]:
                   min_window = (start_index, end_index)
               char_count[s[start_index]] += 1
               target_chars_remaining += 1
               start_index += 1
       return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]
