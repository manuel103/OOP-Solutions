'''
Given a number N and a value K. From the right, set the Kth bit in the binary 
representation of N. The position of Least Significant Bit(or last bit) is 0, 
the second last bit is 1 and so on.

Example 1:

Input:
N = 10 
K = 2
Output:
14
Explanation:
Binary representation of the given number
10 is: 1 0 1 0, number of bits in the 
binary reprsentation is 4. Thus 2nd bit
from right is 0. The number after changing
this bit to 1 is: 14(1 1 1 0).

'''


# class Solution:
#     def setKthBit(self, N, K):
#         binary = "{0:b}".format(int(N))

#         # Convert binary values to individual strings
#         digits = [int(x) for x in str(binary)]

#         # Check the value at position K and replace with 1 if 0
#         if digits[K-1] == 0:
#             digits[K-1] = 1

#         # Convert string binary values back to int
#         strings = [str(x) for x in digits]
#         a_string = "".join(strings)
#         new_binary = int(a_string)

#         #Convert the new binary value to decimal
#         decimal, i = 0, 0
#         while(new_binary != 0):
#             dec = new_binary % 10
#             decimal = decimal + dec * pow(2, i)
#             new_binary = new_binary//10
#             i += 1

#         return decimal


class Solution:
    def setKthBit(self, N, K):

        return ((1 << K) | N)


ans = Solution()
print(ans.setKthBit(384, 7))
