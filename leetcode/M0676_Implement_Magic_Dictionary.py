from typing import List

class MagicDictionary:
    def __init__(self):
        self.data = {}

    def buildDict(self, dict: List[str]) -> None:
        for word in dict:
            length = len(word)
            node = self.data.setdefault(length, {})
            for letter in word:
                node = node.setdefault(letter, {})

    def search(self, word: str) -> bool:
        if not word: return False
        length = len(word)
        if length not in self.data: return False
        def backtrace(node = self.data[length], i = 0, miss = False):
            if i == length: return miss
            for x in node:
                if not miss or x == word[i]:
                    if backtrace(node[x], i + 1, miss or word[i] != x):
                        return True
            return False
        return backtrace()


magic = MagicDictionary()
magic.buildDict(["hello", "leetcode"])
print(False, magic.search("hello"))
print(True, magic.search("hhllo"))
print(False, magic.search("hell"))
print(False, magic.search("leetcoded"))

magic = MagicDictionary()
magic.buildDict(["hello","hallo","leetcode"])
print(True, magic.search("hello"))
print(True, magic.search("hhllo"))
print(False, magic.search("hell"))
print(False, magic.search("leetcoded"))


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

# Implement a magic directory with buildDict, and search methods.

# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-magic-dictionary
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
