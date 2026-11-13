class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        # Assign hashmap for letters
        for letter in s:
            letters_s[letter] = 1 + letters_s.get(letter, 0)

        letters_t = {}
        for letter in t:
            letters_t[letter] = 1 + letters_t.get(letter,0)
        
        if letters_s == letters_t:
            return True
        else:
            return False