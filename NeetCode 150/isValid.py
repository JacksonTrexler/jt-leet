class Solution:
    def isValid(self, s: str) -> bool:
        pending = []
        parenthesisMatch = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in parenthesisMatch.values():
                pending.append(c)
            elif c in parenthesisMatch:
                if not pending or pending.pop() != parenthesisMatch[c]:
                    return False
        return not pending
