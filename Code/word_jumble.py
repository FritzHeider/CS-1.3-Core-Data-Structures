import collections
import itertools
import sys
import time

def timer(func):
    """Wraps func in time logic."""
    def _timer(*args):
        start_time = time.time()
        res = func(*args)
        end_time = time.time()
        print(end_time - start_time)
        return res
    return _timer

def permutations(word):
    """Recursively generates permutations of word"""
    def _perms(i):
        if i == len(arr):
            res.append(arr[:])
        else:
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                _perms(i+1)
                arr[i], arr[j] = arr[j], arr[i]
    res = []
    arr = list(word)
    _perms(0)
    return set(map("".join, res))

def possible_words_for_jumble(words, jumble):
    """Finds the next possible word permutation of jumble."""
    for word in words:
        word = word.strip("\n")
        if (len(word) == len(jumble) and
            collections.Counter(word) == collections.Counter(jumble)):
            yield word

def slow_possible_words_for_jumble(words, jumble):
    """Finds the next possible word permutation of jumble with slow
    permutations."""
    word_set = set(map(lambda word: word.strip("\n"), words))
    for permutation in permutations(jumble):
        if permutation in word_set:
            yield permutation

if __name__ == "__main__":
    """Pass a jumbled word as a command line argument"""
    if len(sys.argv) < 2:
        with open("/usr/share/dict/words", "r") as words_file:
            for jumble in ("laisa", "laurr", "bureek", "prouot"):
                words_file, words = itertools.tee(words_file) # make copy of file
                print(f"jumble: {jumble} "
                      f"possible words: "
                      f"{tuple(slow_possible_words_for_jumble(words, jumble))}")
        sys.exit(0)

    ##                                                                        ##
    ## ~~~~~~~~~~~~~~~~~~~~~~~~ With histograms: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
    with open("/usr/share/dict/words", "r") as words_file:
        print(tuple(possible_words_for_jumble(words_file, sys.argv[1])))


    ##                                                                        ##
    ## ~~~~~~~~~~~~~~~~~~~~~~~~~ In one line: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
    # print(tuple(word_ for word in open("/usr/share/dict/words", "r")
    #             if (len(word_ := word.strip("\n")) == len(sys.argv[1]) and
    #                 (collections.Counter(word_) ==
    #                  collections.Counter(sys.argv[1])))))

    ##                                                                        ##
    ## ~~~~~~~~~~~~~~~~~~~~~~ With permutations: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
    # with open("/usr/share/dict/words", "r") as words_file:
    #     print(tuple(slow_possible_words_for_jumble(words_file, sys.argv[1])))
