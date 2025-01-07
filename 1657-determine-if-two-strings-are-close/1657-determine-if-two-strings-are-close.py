class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        d1 = Counter(word1)
        d2 = Counter(word2)

        f1 = list(d1.values())
        f2 = list(d2.values())

        f1.sort()
        f2.sort()

        return f1 == f2
