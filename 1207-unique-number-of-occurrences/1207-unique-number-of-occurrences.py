class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        print(d)
        temp = set()
        for digit,occurance in d.items():
            if occurance not in temp:
                temp.add(occurance)
            else:
                return False
        return True