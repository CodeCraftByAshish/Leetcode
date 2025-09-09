class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        op = [[] for _ in range(numRows)]
        count, step = 0,1
        for ch in s:
            op[count].append(ch)
            count = count + step
            if count == numRows - 1 or count == 0:
                step *= -1
        return "".join(["".join(val) for val in op])


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 4))
