class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        open = {"(","[","{"}

        for c in s:
            if c in open:
                stack.append(c)
                continue

            if not stack:
                return False
            if c != closed[stack[len(stack)-1]]:
                return False
            else:
                stack.pop()
        return len(stack) == 0


        