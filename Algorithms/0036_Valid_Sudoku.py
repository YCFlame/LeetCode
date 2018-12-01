#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        bitmap = {str(i) + str(j): 0 for i in range(3) for j in range(3)}
        for i in range(9):
            bitmap['row%s' % i] = 0
            bitmap['col%s' % i] = 0

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == '.':
                    continue

                if not digit.isdigit():
                    return False

                digit = int(digit)

                if digit > 9 or digit < 1:
                    return False

                if bitmap['row%s' % i] & (1 << digit) or bitmap['col%s' % j] & (1 << digit) or bitmap[str(i / 3) + str(j / 3)] & (1 << digit):
                    return False
                else:
                    bitmap['row%s' % i] |= (1 << digit)
                    bitmap['col%s' % j] |= (1 << digit)
                    bitmap[str(i / 3) + str(j / 3)] |= (1 << digit)

        return True
