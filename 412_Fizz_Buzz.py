
class Solution:
    def fizzBuzz(self, n: int) -> "List[str]":
        result = []
        for i in range(1, n+1):
            check_result = ""
            if i % 3 == 0:
                check_result = "Fizz"
            if i % 5 == 0:
                check_result += "Buzz"
            if check_result == "":
                check_result = str(i)
            result.append(check_result)

        return result

processor = Solution()
print(processor.fizzBuzz(15))