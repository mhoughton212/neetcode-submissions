class Solution:
    #5#Hello5#World

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}!{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "!":
                j += 1
            str_len = int(s[i:j])
            start = j + 1
            end = start + str_len
            res.append(s[start: end])
            i = end
        return res
        