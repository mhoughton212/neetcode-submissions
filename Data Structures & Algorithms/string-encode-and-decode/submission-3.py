class Solution:
    #5#Hello5#World

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}!{s}"
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        j = 0
        i = 0
        while i < len(s):
            while s[j] != "!":
                j += 1
            print(s[i:j])
            str_len = int(s[i:j])
            start = j + 1
            end = start + str_len
            res.append(s[start: end])
            i = j = end
        return res
        