class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(T))]
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                index = stack.pop()
                result[index] = i - index
            
            stack.append(i)
            
        return result

"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            if T[i] < T[i + 1]:
                result[i] = 1
            else:
                k = i + 1
                while k < len(T):
                    if result[k] == 0:
                        result[i] = 0
                        break
                    else:
                        k += result[k]
                        if T[i] < T[k]:
                            result[i] = k - i
                            break
            
        return result
"""
