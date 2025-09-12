class Solution:
    def reverse(self, x: int) -> int:
        expr = -1 if x<0 else 1
        x = expr*x
        op = x%10
        while x:=x//10:
            op = x%10 + op*10
        
        x = op*expr
        if (x>=0 and x > (2**31)-1) or (x<0 and x<-2**31):
            return 0
        return x


if __name__ == "__main__":
    print(Solution().reverse(1534236469))
