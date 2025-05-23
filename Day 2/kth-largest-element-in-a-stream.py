class KthLargest:


   def __init__(self, k: int, nums: List[int]):
       self.k = k
       nums.sort()
       self.stream = nums
       if k > len(nums):
           self.curr = None
       else:
           self.curr = nums[len(nums)-k]


   def add(self, val: int) -> int:
       self.stream.append(val)
       self.stream.sort()
       self.curr = self.stream[len(self.stream)-self.k]
       return self.curr
      




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
