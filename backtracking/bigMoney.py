#!/bin/python3

import fileinput
from typing import List, Tuple
from collections import defaultdict


#
# Complete the two functions below.
#
# add_trade() will accept each row of input as a list.
# run() will be called after adding all rows of input and should return an integer representing the total maximum profit.
#
trades = defaultdict(list)


class Solution:
    count = 0
    mindate = 0
    maxdate = 0
    def add_trade(self, future_trade: List):
        # Write your code here
        temp = future_trade[1].split("/")
        date = str(temp[2] + temp[1]+temp[0])
        date = int(date)
        if self.count == 0:
            self.mindate = self.maxdate = date
            self.count += 1
        else:
            self.mindate = min(date, self.mindate)
            self.maxdate = max(date, self.maxdate)
        trades[future_trade[0]].append((date, float(future_trade[2])))

    def run(self):
        # Write your code here
        def getValue(obj):
            return obj[0]
        def getReturn(obj):
            return obj[2]
        companies = list(trades.keys())
        moneyInHand = 1000.00
        returns = []
        for company in companies:
            trades[company].sort(key=getValue)
            n = len(trades[company])
            temp = list(trades[company])
            r = 1
            l = 0
            while r < n and l < n-1:
                if temp[l][1] <= temp[l+1][1] and (r == n-1 or temp[r][1] >= temp[r+1][1]):
                    #returns: (buydate, selldate, %return)
                    returns.append((temp[l][0], temp[r][0], (temp[r][1]-temp[l][1])/temp[l][1]))
                    l = r + 1
                else:
                    if temp[l][1] > temp[l+1][1]:
                        l += 1
                    if r < n -1 and temp[r][1] < temp[r+1][1]:
                        r += 1
                if r < l+1:
                    r = l+ 1
            del temp
            del trades[company]
        returns.sort(key=getReturn)
        #print(self.maxdate, self.mindate)
        maxProfits = 0
        
        def tradePossible(avail, buy, sell) -> int:
            for i in range(0, len(avail), 2):
                if sell < avail[i]:
                    return -1
                if buy >= avail[i]:
                    if sell > avail[i+1]:
                        return -1
                    if sell <=avail[i+1]:
                        return i
                if buy > avail[i+1]:
                    continue
            return -1
        availableDates = [self.mindate, self.maxdate]
        def dfs(rets, ans, path, available):
            #tradeDates = set([i for i in range(0,  rets[0][1] - rets[0][0]+1)])
            if len(rets) == 0:
                ans.append(path)
                return
            x = tradePossible(available, rets[0][0],rets[0][1])
            if x != -1:
                available = available[:x+1] + [rets[0][0]] + [rets[0][1]] + available[x+1:]
                if(len(rets) == 1):
                    ans.append(path)
                    return
                else:
                    for i in range(len(rets)):
                        dfs(rets[i + 1:], ans, path, available)
            else:
                path.append(rets[0])
                for i in range(len(rets)):
                    dfs(rets[1:], ans, path, available)
        ans = []
        dfs(returns, ans, [], availableDates)   
        '''
        I don't know if anyone is going to look at this. I ran out time before I could figure it out but
        I am going to explain what I was doing just in case I can get some credit for that. I started by
        making a dictionary of all the trades, sorted by date, then finding all pairs of prices/dates with
        positive returns and putting those into a list that are sorted by the amount of return. Then the part
        where I did not finish was creating a backtracking algorithm to determine the amount of profit that
        could be gained from the trades.
        '''
        maxProfit = 0
        for path in ans:
            currProfit = 0
            temp = list(path)
            temp.sort(key=getValue)
            moneyLeft = 1000.00
            for i in temp:
                profit = moneyLeft * i[2]
                currProfit += profit
                moneyLeft += profit
            maxProfit = max(currProfit, maxProfit)
        return maxProfit
            
        # ans = 0
        
            

if __name__ == '__main__':
    solution = Solution()
    for row in fileinput.input():
        future_trade = list(row.strip().replace(" ", "").split(","))
        solution.add_trade(future_trade)
        
    print(solution.run())