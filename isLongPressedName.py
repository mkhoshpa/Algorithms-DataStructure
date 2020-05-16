class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        def checkOneChar(name, typed):
            print(name)
            print(typed)
            print()
            if len(typed) < len(name):
                return False, None, None
            if len(name) == 0:
                if len(typed) == 0:
                    return True, 0, 0
                return False, None, None
            i = 0
            pointer = 0
            while i < len(name) - 1:
                if name[i] == name[i + 1]:
                    i += 1
                else:
                    break

            while pointer < len(typed) - 1:
                if typed[pointer] == typed[pointer + 1]:
                    pointer += 1
                else:
                    break
            if name[0] == typed[0] and i <= pointer:
                return True, i + 1, pointer + 1
            return False, None, None

        while True:
            b, num_name, num_typed = checkOneChar(name, typed)
            if not b:
                return False
            if num_name == 0:
                return True
            name = name[num_name:]
            typed = typed[num_typed:]


def main():
    nums =[1]
    s = Solution()
    print(s.isLongPressedName('leelee','lleeelee'))

if __name__ == '__main__':
    main()