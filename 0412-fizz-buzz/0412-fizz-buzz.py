class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        string_list = []
        # for i in range(1, n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         string_list.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         string_list.append("Fizz")
        #     elif i % 5 == 0:
        #         string_list.append("Buzz")
        #     else:
        #         string_list.append(str(i))

        for i in range(1, n + 1):
            string_list.append(str(i))
        for i in range(2, n, 3):
            string_list[i] = "Fizz"
        for i in range(4, n, 5):
            string_list[i] = "Buzz"
        for i in range(14, n, 15):
            string_list[i] = "FizzBuzz"

        return string_list
