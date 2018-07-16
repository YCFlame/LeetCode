#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        round = 0
        n = len(matrix[0])
        while round < n / 2:
            for i in range(round, n - round - 1):
                j, k = round, i
                prev = matrix[j][k]
                for _ in range(4):
                    j, k = k, n - j - 1
                    temp = matrix[j][k]
                    matrix[j][k] = prev
                    prev = temp

            round += 1

        """
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        """
