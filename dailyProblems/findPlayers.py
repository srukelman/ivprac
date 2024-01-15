'''
Runtime: beats 72.28%
Memory: beats 27.12%
'''

from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        winners = defaultdict(int)
        players = set()
        for match in matches:
            losses[match[1]] += 1
            winners[match[0]] += 1
            players.add(match[1])
            players.add(match[0])

        no_loss, one_loss = [], []
        for player in players:
            if losses[player] == 1:
                one_loss.append(player)
            elif losses[player] == 0:
                no_loss.append(player)
        return [sorted(no_loss), sorted(one_loss)]
        