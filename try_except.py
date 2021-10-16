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
    print(tmp,s)
    tmp.reverse()
    print(tmp,s)

    if tmp == s:
        print(tmp, s)
        return True
    else:
        return False

def word(n):
    result = []
    for i in range(n):
        element = input('Enter element: ')
        result.append(element)

    if is_palindrome(result):
        print(f'{result} - is palindrome')
    else:
        print('not palindrom')

word(3)