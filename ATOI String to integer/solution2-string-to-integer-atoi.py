class Solution:
    def myAtoi(self, s: str) -> int:
        intlist = ["0","1","2","3","4","5","6","7","8","9"]
        expr = 1
        op = []
        for i in s:
            if not op:
                if i == " ":
                    continue
                if i in ["-", "+"] or i in intlist:
                    if i == "-":
                        expr = -1
                    if i in ["-", "+"]:
                        i = "0"
                    op.append(i)
                else:
                    break
            elif i in intlist:
                op.append(i)
            else:
                break
        op = (int("".join(op)) if op else 0) * expr
        const = 2**31
        return -const if op<0 and op <-const else const-1 if op>=0 and op >= const else op
