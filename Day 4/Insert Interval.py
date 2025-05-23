class Solution:
   def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       #Thoughts
       '''
       store the min and max of the new interval, loop through indicies of
       the original interval and build our interval that way i suppose
       '''
       l, r = [],[]
       for interval in intervals:
           if interval[1] < newInterval[0]:
               l.append(interval)
           elif interval[0] > newInterval[1]:
               r.append(interval)
           else:
               newInterval = [min(interval[0], newInterval[0]),
               max(interval[1],newInterval[1])]
       return l + newInterval + r   