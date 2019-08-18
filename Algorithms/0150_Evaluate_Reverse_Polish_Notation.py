class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from operator import add, sub, mul
        def div(a, b):
            return 
        stack = []
        ops = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda a, b: int(a / b),
        }
        for c in tokens:
            if c in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[c](a, b))
            else:
                stack.append(int(c))
                            
        return stack[0]
