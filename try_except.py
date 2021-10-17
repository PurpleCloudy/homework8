# while True:
#     try:
#         n = input('enter int: ')
#         n = int(n)
#         break
#     except ValueError:
#         print('input not int try again')
# print('success')


def is_palindrome(s):
    tmp = s[:]
    tmp.reverse()


    if tmp == s:
        print(tmp, s)
        return True
    else:
        return False

def word(n):
    ''' input: n - int
    uses n as range value for cheating list with strings
    output: print() - with data returned by is palindrome() function
    '''
    result = []
    for i in range(n):
        element = input('Enter element: ')
        result.append(element)

    if is_palindrome(result):
        print(f'{result} - is palindrome')
    else:
        print(f'{result} - not palindrom')

word(3)