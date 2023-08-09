class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        begin = 0
        end = 0
        counter = 0
        maxlen = 0
        prevend = -1
        while(end < len(nums)):
            numb = nums[begin]
            nume = nums[end]
            if(nume == 0 and end != prevend):
                counter += 1
            prevend = end
            if(counter <= k):
                end += 1
                if((end - begin) > maxlen):
                    maxlen = end-begin  
            elif(counter > k):
                if(numb == 0):
                    counter -= 1
                begin += 1
                if(end < begin):
                    end = begin
                    counter = 0
        if(counter <= k and (end - begin) > maxlen):
                maxlen = end-begin
        return maxlen