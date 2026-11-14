class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # if word not in sequence:
        #     return 0
        # return sequence.count(word)
        temp, res = word, 0
        while temp in sequence:
            res += 1
            temp += word
        return res