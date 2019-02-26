class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapper = {word: index for index, word in enumerate(list1)}
        result = []
        for i, word in enumerate(list2):
            if word in mapper:
                sum = i + mapper[word]
                if not result or sum < result[0][0]:
                    result = [(sum, word)]
                elif sum == result[0][0]:
                    result.append((sum, word))
        
        return [word for _, word in result]
