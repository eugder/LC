class Roman2Int:
    def convert(self, roman: str) -> int:
        numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        pre = 0
        result = 0
        for i in reversed(roman):
            if numbers[i] < pre:
                result = result - numbers[i]
            else:
                result = result + numbers[i]
            pre = numbers[i]
        return result
