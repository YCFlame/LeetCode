class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 1
        if name[0] != typed[0]:
            return False
        last = name[0]
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                last = name[i]
                i += 1
                j += 1
            elif typed[j] == last:
                j += 1
            else:
                return False
        
        if i < len(name):
            return False
        while j < len(name):
            if typed[j] != last:
                return False
            
        return True
            
