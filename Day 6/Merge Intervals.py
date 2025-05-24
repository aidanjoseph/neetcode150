class Solution:
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       #thoughts
       '''
       loop through whole thing
       basically if end < start next,
       we append
       Cases:
           if end < start next
               append interval
               update start and ends
           if end == start next
               update end == end next,
           if end > start next:
               if end > end next, then similar stuff as above
       '''
       finalArray = []
       if len(intervals) == 0:
           return finalArray
       if len(intervals) == 1:
           return intervals
       intervals.sort()
       currStart = intervals[0][0]
       currEnd = intervals[0][1]
       for i in range(1, len(intervals)):
           startNext = intervals[i][0]
           endNext = intervals[i][1]
           if currEnd < startNext:
               finalArray.append([currStart,currEnd])
               currStart = startNext
               currEnd = endNext
               continue
           elif (currEnd == startNext):
               currEnd = endNext
           if currEnd > startNext:
               if currEnd < endNext:
                   currEnd = endNext
           if i == (len(intervals) - 1):
               finalArray.append([currStart, currEnd])
       if intervals[-1][0] > finalArray[-1][1]:
           finalArray.append(intervals[-1])
       return finalArray


