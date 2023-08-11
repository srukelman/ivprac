from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        mid = 0
        high = n-1
        row = -1
        while low <= high:
            mid = (high + low)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid][-1] > target:
                row = mid
                break
            elif matrix[mid][0] > target:
                if mid == 0:
                    return False
                if matrix[mid-1][-1] < target:
                    return False
                high = mid - 1
            elif matrix[mid][-1] < target:
                if mid == n-1:
                    return False
                if matrix[mid+1][0] > target:
                    return False
                low = mid + 1
        nums = matrix[row]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                if mid == len(nums)-1:
                    return False
                low = mid + 1
            if nums[mid] > target:
                if mid == low:
                    return False
                high = mid - 1
        return False
