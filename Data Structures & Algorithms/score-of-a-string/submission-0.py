class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = list(map(ord, s))
        result=0

        for i in range(len(ascii_values)-1):
            result += abs(ascii_values[i] - ascii_values[i+1])
        return result