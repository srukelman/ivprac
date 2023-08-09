class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        begin = 0
        end = 0
        maxlen = 0
        while(end <= len(nums)):
            try:
                num = nums[end]
            except:
                num = 0
            if(num == 0):
                if((end-begin) > maxlen):
                    maxlen = end - begin
                begin = end + 1
                end = begin
            else:
                end += 1
        return maxlen