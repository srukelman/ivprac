class Solution:
    def longestSentence(S):
        arr = S.split(" ")
        max_len = 0
        begin = 0
        end = 0
        l = ['!', '.', '?']
        emptyCount = 0
        while end < len(arr):
            if(len(arr[end]) == 0):
                emptyCount += 1
                end += 1
                continue
            eos = [i for i in l if i in arr[end]]
            if eos:
                if end - begin - emptyCount + 1> max_len:
                    max_len = end - begin - emptyCount + 1
                begin = end + 1
                emptyCount = 0
            else:
                end += 1
        if end - begin - emptyCount > max_len:
            max_len = end - begin - emptyCount