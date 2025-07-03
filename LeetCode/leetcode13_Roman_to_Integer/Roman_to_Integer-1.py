class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1, 5, 10, 50, 100, 500, 1000]
        symbols_to_values = dict(zip(symbols, values))
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and symbols_to_values[s[i]] < symbols_to_values[s[i + 1]]:
                total -= symbols_to_values[s[i]]
            else:
                total += symbols_to_values[s[i]]


        return total
        


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV")) # 1994
