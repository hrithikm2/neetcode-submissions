class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, encoded: str) -> List[str]:
        result = []
        i = 0

        while i < len(encoded):
            delimiter_index = encoded.find("#", i)
            if delimiter_index == -1:
                break

            length = int(encoded[i:delimiter_index])
            start = delimiter_index + 1
            end = start + length

            result.append(encoded[start:end])
            i = end

        return result
