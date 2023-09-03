'''
IBM Interview Question
Given an array of integers in which each element represents the skill of a person.
Each person needs to be paired with another person to form a team.
Each team must have the same overall skill (the sum of the skills of the team members).
Return the sum of the efficiencies of the teams (the product of the skills of the team members).
Solutions are unique.
'''
from typing import List
def getTotalEfficiency(skill: List[int]) -> int:
    skill.sort()
    target = sum(skill)/(len(skill)//2)
    s = 0
    for i in range(len(skill)//2):
        if skill[i] + skill[-i-1] == target:
            s += skill[i]*skill[len(skill)-1-i]
        else:
            return -1
    return s
        