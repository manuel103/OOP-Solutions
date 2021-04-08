'''
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

# Method 1: Brute force approach with O(n2)


# def isUnique(str: str):
#     for i in range(len(str)):
#         for j in range(i + 1, len(str)):
#             if str[i] == str[j]:
#                 return False
#     return True


# solution = isUnique("Japol0")
# print(solution)


''' Method 2: ASCII sorting => O(n log n) '''




import time
from collections import defaultdict
import unittest
def isUnique(str: str):
    sorted_str = sorted(str)
    for i in range(len(sorted_str)-1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        # non-unique 129 chars
        ("".join([chr(val // 2) for val in range(129)]), False),
    ]
    test_functions = [
        isUnique
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
