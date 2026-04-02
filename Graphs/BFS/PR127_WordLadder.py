from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Word Ladder Problem:
        --------------------
        Given a start word, an end word, and a dictionary of words,
        find the shortest transformation sequence length such that:
        - Only one letter can be changed at a time
        - Each transformed word must exist in the dictionary

        Approach:
        ---------
        We use Breadth-First Search (BFS):
        - Treat each word as a node in a graph
        - Connect words that differ by exactly one letter
        - BFS guarantees the shortest path when we reach endWord

        Diagram (example: hit -> cog):
        
            Level 1: hit
                      |
            Level 2: hot
                      |
            Level 3: dot, lot
                      |
            Level 4: dog, log
                      |
            Level 5: cog  ✅ found

        Answer = 5 steps
        """

        chars = "abcdefghijklmnopqrstuvwxyz"
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # queue holds (word, steps)
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            # take the first word from queue
            wo, le = queue.popleft()

            # if we reached the target word, return steps
            if wo == endWord:
                return le

            # try changing each character in the word
            for i in range(len(wo)):
                for x in chars:
                    pattern = wo[:i] + x + wo[i+1:]
                    # if new word is valid and not visited
                    if pattern in wordSet and pattern not in visited:
                        queue.append((pattern, le + 1))  # add to queue with +1 step
                        wordSet.remove(pattern)          # remove from dictionary
                        visited.add(pattern)             # mark visited

        # if no path found
        return 0
