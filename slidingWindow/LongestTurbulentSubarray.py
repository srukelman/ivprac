class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        begin = 0
        end = 0
        prevend = -1
        maxlen = 0
        prevsign = ""
        currsign = ""
        while(end < len(arr)):
            if(arr[end] > arr[end-1]):
                currsign = "<"
            elif(arr[end] < arr[end-1]):
                currsign = ">"
            else:
                begin = end
                end = begin + 1
            if(currsign != prevsign):
                end += 1
                prevsign = currsign
                if((end - begin) > maxlen):
                    maxlen = end - begin
            else:
                begin = end - 1
                end = begin + 1
                prevsign = ""
            
        if((end - begin) > maxlen):
            maxlen = end-begin
        return maxlen