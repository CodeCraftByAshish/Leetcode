class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"[":"]", "{":"}", "(":")"}
        next_parentheses = []
        for i in s:
            if val:=parentheses.get(i):
                next_parentheses.append(val)
            elif next_parentheses and i == next_parentheses[-1]:
                next_parentheses.pop()
            else:
                return False
        return False if next_parentheses else True
            
if __name__ == "__main__":
    print(Solution().isValid("({[}]})"))