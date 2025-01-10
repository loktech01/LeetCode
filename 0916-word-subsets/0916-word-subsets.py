class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        mx_freq = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char, freq in word_freq.items():
                mx_freq[char] = max(mx_freq[char],freq)
        
        for word in words1:
            word_freq = Counter(word)
            if all(word_freq[char] >= mx_freq[char] for char in mx_freq):
                ans.append(word)
        return ans