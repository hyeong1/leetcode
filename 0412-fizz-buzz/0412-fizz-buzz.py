class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        string_list = []
        for i in range(1, n + 1):
            string_list.append(str(i))

        for i in range(1, n+1):
            entry = ""
            if i % 3 == 0:
                entry += "Fizz"
            if i % 5 == 0:
                entry += "Buzz"
            if i % 3 == 0 or i % 5 == 0:
                string_list[i-1] = entry

        return string_list
