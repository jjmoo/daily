class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self._to_end(word, True)
        node['$'] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._to_end(word)
        return bool(node) and '$' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._to_end(prefix)
        return bool(node)

    def _to_end(self, word: str, insert = False) -> dict:
        node = self.root
        for ch in word:
            if insert and ch not in node:
                node[ch] = {}
            if ch in node:
                node = node[ch]
            else:
                return None
        return node


trie = Trie()
print(None, trie.insert("apple"))
print(True, trie.search("apple"))
print(False, trie.search("app"))
print(True, trie.startsWith("app"))
print(None, trie.insert("app"))
print(True, trie.search("app"))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
