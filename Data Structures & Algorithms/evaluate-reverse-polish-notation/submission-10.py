class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = ("-", "*", "+", "/")

        for n in tokens:
            if n not in operators:
                stack.append(n)
            else:
                n1, n2 = stack.pop(), stack.pop()
                n1, n2 = int(n1), int(n2)
                res = 0
                if n == "-":
                    res = n2 - n1
                elif n == "+":
                    res = n2 + n1
                elif n == "*":
                    res = n2 * n1
                elif n == "/":
                    res = n2 / n1
                stack.append(res)
        return int(stack[0])
