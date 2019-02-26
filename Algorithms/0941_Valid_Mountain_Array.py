class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        up = down = False
        if len(A) < 3:
            return False
        
        last = A[0]
        for n in A[1:]:
            if n == last:
                return False
            elif n > last:
                if down:
                    return False
                up = True
            else:
                if not up:
                    return False              
                down = True
            
            last = n
                
        return up and down
        
  
  
  """
  class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
  """
