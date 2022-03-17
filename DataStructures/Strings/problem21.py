"""
Given a word (ab) and a string (abxaba)
return list of indexes which are starting locations of
anagrams of the word
"""
from collections import Counter


def solve(word, string):
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    result = []
    for i in range(len(string) - len(word)+1):
        window = string[i:i+len(word)]

        if is_anagram(window, word):
            result.append(i)

    return result




