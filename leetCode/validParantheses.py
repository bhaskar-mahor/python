class Solution:
    def isValid(self, str: str) -> bool:
        str = str.strip()
        length = len(str)
        if length == 0:
            return True
        elif length %2 != 0:
            return False
        else:
            while '()' in str or '{}' in str or '[]' in str:
                str = str.replace('{}', '').replace('()', '').replace('[]', '')
            if str != '':
                return False
            else:
                return True


obj = Solution()
print(obj.isValid("{[]}"))