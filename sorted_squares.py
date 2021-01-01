"""This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in
sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81]."""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([(i**2) for i in nums])
