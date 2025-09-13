class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        first_val = s[0]
        expr = -1 if first_val == "-" else 1
        if first_val in ["-", "+"]:
            s = s[1:]
        op = 0
        for i in s:
            if i.isdigit():
                op = op*10 + int(i)
            else:
                break
        print(op, expr)
        op = op * expr
        mininum, maximum = 2**31 * -1, 2**31-1
        return max(mininum, min(maximum, op))


if __name__ == "__main__":
    print(Solution().myAtoi("  -042"))


