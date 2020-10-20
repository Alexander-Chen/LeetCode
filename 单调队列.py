from collections import deque
from typing import List
class MonotonicQueue(object):
    def __init__(self,maxlen):
        self.data=deque(maxlen=maxlen)
    def push(self,n):
        while self.data and self.data[-1]<n:
            self.data.pop()
        self.data.append(n)
    def pop(self,n):
        if self.data and self.data[0]==n:            
            self.data.popleft()
    def max(self):
        return self.data[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m=MonotonicQueue(k)
        res=[]
        for i in range(len(nums)):
            if i<k-1:
                m.push(nums[i])
            else:
                m.push(nums[i])
                res.append(m.max())
                m.pop(nums[i-k+1])
        return res

            
s=Solution()
nums = [1,3,-1,-3,5,3,6,7]
k=3
print(s.maxSlidingWindow(nums,k))