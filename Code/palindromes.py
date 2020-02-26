#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casingO(log(2)n)'."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    #return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    left = 0
    right = len(text) - 1
    while left < right:
        while not text[left].isalpha() and left < right:
            left += 1
        while not text[right].isalpha() and left < right:
            right -= 1
        if left < right and text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
def is_palindrome_recursive(text, left=None, right=None):
    #O(log(2)n)
    # TODO: implement the is_palindrome function recursively here
#if length is one or less return true
    if len(text) <= 1:
        return True

    while len(text) > 0 and not text[0].isalpha():
        text = text[1:]

    while len(text) > 0 and not text[len(text)-1].isalpha():
        text = text[:len(text)-1]

    if text[0].lower() != text[len(text)-1].lower():
        return False
    else:
        text = text[1:len(text)-1]

    while len(text) > 0 and not text[0].isalpha():
        text = text[1:]
    while len(text) > 0 and not text[len(text)-1].isalpha():
        text = text[:len(text)-1]

    return is_palindrome_recursive(text)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
