'''
242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''

from collections import Counter #counts the frequency of each element in a hashmap
class Solution: 
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
    
'''
an alternative approach is to create two distinct dicts and for each character, 
do this 

count[s[i]] = 1 + countS.get(s[i], 0) == this is the default for get 
count[s[i]] = 1 + countT.get(t[i], 0) == defualt return is 0

check if they are equal
'''