class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapper = {}
        minimum = 10000
        result = []
        for i, r in enumerate(list1):
            mapper[r] = i
        for i, r in enumerate(list2):
            if r in mapper:
                if i + mapper[r] < minimum:
                    result = [r] 
                    minimum = i + mapper[r]
                elif i + mapper[r] == minimum:
                    result.append(r)
        
        return result
