
class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {}
        bracketMap[')'] = '('
        bracketMap['}'] = '{'
        bracketMap[']'] = '['

        stk = []

        for c in s:
            if c in bracketMap.values(): # 여는 괄호
                stk.append(c)
            elif c in bracketMap.keys(): # 닫는 괄호
                # 비어 있거나, 스택에 들어 있는 값이 c의 여는 괄호가 아니라면 유효한 괄호 문자열이 아니다.
                if len(stk) == 0 or stk.pop() != bracketMap.get(c):
                    return False

        return len(stk) == 0