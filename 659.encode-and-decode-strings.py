class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        enstr = ""
        for word in strs:
            for l in word:
                enstr += f"{ord(l)}-"
            enstr = f"{enstr[:-1]}@"
        return enstr[:-1]

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        strs = str.split("@")
        n = len(strs)
        for i in range(n):
            strs[i] = "".join(chr(int(l)) for l in strs[i].split("-"))
        return strs
        # write your code here


if __name__ == "__main__":
    arr = ["lint", "code", "love", "you"]
    sol = Solution()
    word = sol.encode(arr)
    print(word)
    word = sol.decode(word)
    print(word)
