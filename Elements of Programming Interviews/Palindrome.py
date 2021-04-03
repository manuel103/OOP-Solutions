'''All methods have space complexity of O(n) & time complexity of O(1)'''

'''Method 1 (Using a temp variable)'''

def palindromeCheck(str):
    store = ''
    for char in str:
        store = store + char
    if str == store[::-1]:
        return True
    return False

'''Method 2 (Recursive approach)'''


def palindromeCheck(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True


'''Method 3 (Using inbuilt python functions)'''


def palindromeCheck(str):
    # reverse string
    rev = ''.join(reversed(str))
    if str == rev:
        return True
    return False


string = 'malilam'
print(palindromeCheck(string))
