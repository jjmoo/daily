from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        result, trie = [], {}
        for word in words:
            node = self._to_end(trie, word)
            if node is not None:
                if '$' in node: continue
                result.append(word)
            else:
                exist, length = self._search_word(board, word)
                if not exist:
                    word = word[:length + 1] + '$'
                else:
                    result.append(word)
                self._to_end(trie, word, True)
        return result

    def _to_end(self, node: dict, word: str, insert = False) -> dict:
        for ch in word:
            if insert and ch not in node:
                node[ch] = {}
            if ch in node:
                node = node[ch]
            elif '$' in node:
                break
            else:
                return None
        return node

    def _search_word(self, board: List[List[str]], word: str) -> bool:
        n, m, l = len(board), len(board[0]), len(word)
        found, table = 0, [[False] * m for _ in range(n)]
        def backtrace(i, j, k = 1):
            if k == l: return True
            choice = []
            if i - 1 >= 0 and not table[i - 1][j]: choice.append((i - 1, j))
            if i + 1 < n and not table[i + 1][j]: choice.append((i + 1, j))
            if j - 1 >= 0 and not table[i][j - 1]: choice.append((i, j - 1))
            if j + 1 < m and not table[i][j + 1]: choice.append((i, j + 1))
            if choice: nonlocal found
            for ci, cj in choice:
                if board[ci][cj] == word[k]:
                    found = max(found, k + 1)
                    table[ci][cj] = True
                    if backtrace(ci, cj, k + 1): return True
                    table[ci][cj] = False
            return False
        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    found = max(found, 1)
                    table[i][j] = True
                    if backtrace(i, j): return True, found
                    table[i][j] = False
        return False, found


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['$'] = word
        def backtrace(i, j, p = trie):
            ch = board[i][j]
            node = p[ch]
            word = node.pop('$', False)
            if word:
                result.append(word)
            board[i][j] = '#'
            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + ii, j + jj
                if 0 <= ni and ni < n and 0 <= nj and nj < m and board[ni][nj] in node:
                    backtrace(ni, nj, node)
            board[i][j] = ch
            if not node: p.pop(ch)
        n, m, result = len(board), len(board[0]), []
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    backtrace(i, j)
        return result


test = Solution2().findWords
print(test([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oath","pea","eat","rain","ea","eab","eatk","eatkb"]))
print(test([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oah","oahk"]))


# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example:

# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

# words = ["oath","pea","eat","rain"]

# Output: ["eat","oath"]

# Note:

# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
