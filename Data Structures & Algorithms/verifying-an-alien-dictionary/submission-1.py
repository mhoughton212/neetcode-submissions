class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]

            for j in range(len(word1)):
                if j == len(word2):
                    return False
                
                c1, c2 = word1[j], word2[j]
                if c1 != c2:
                    if order_map[c1] > order_map[c2]:
                        return False
                    else:
                        break

        return True