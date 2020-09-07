'''
    Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

'''

class Solution:
    def wordPattern(self, pattern, s):
        d_symb, d_word, words = {}, {}, s.split()
        if len(words) != len(pattern): return False
        for symb, word in zip(pattern, words):
            if symb not in d_symb:
                if word in d_word: return False
                else:
                    d_symb[symb] = word
                    d_word[word] = symb
            elif d_symb[symb] != word: return False
        return True