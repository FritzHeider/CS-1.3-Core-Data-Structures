#!python


def start_new(text, pattern, index):
    for letter in range(index, len(text) - len(pattern) + 1):
        if text[letter] == pattern[0]:
            return letter
    return None

def match(text, pattern, index):
    for match in range(len(pattern)):
        if text[index + match] != pattern[match]:
            return False
    return True

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    best case O(1) worst case O(n)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if len(pattern) == 0:
        return True
    starter = start_new(text, pattern, 0)
    while starter is not None:
        if match(text, pattern, starter):
            return True
        starter = start_new(text, pattern, starter+1)

    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text
    best case O(n) worst case O(n),
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if len(pattern) == 0:
        return 0
    starter = start_new(text, pattern, 0)
    while starter is not None:
        if match(text, pattern, starter):
            return starter
        starter = start_new(text, pattern, starter+1)



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text
    best case O(n) worst case O(n),
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    start_index = []

    if len(pattern) == 0:
        for starter in range(len(text)):
            start_index.append(starter)
    else:
        starter = start_new(text, pattern, 0)
        while starter is not None:
            if match(text, pattern, starter):
                start_index.append(starter)
            starter = start_new(text, pattern, starter+1)
    return start_index

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
