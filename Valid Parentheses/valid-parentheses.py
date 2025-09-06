class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"[":"]", "{":"}", "(":")"}
        op = []
        for i in s:
            if val:=parentheses.get(i):
                op.append(val)
            elif op and i == op[-1]:
                op.pop()
            else:
                return False
        return False if op else True
            
if __name__ == "__main__":
    print(Solution().isValid("({[]})"))