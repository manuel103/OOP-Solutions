'''
Write a function which takes a string s as input, and
returns true if the characters in s can be permuted to form a string that is 
palindromic,
i.e., reads the same backwards as forwards. 

For example, your function should return
true for “GATTAACAG”, since “GATACATAG” is a permutation of this string 
and is palindromic
'''


def isPalindromic(S):
    char_list = []
    # For each character in input strings,
    # remove character if listt contains
    # else add character to listt
    for i in range(len(S)):
        if S[i] in char_list:
            char_list.remove(S[i])
        else:
            char_list.append(S[i])

    if len(S) % 2 == 0 and len(char_list) == 0:
        return True
    elif len(S) % 2 == 1 and len(char_list) == 1:
        return True
    else:
        return False


print(isPalindromic("GATTAACAG"))
