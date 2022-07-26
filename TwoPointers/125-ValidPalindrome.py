class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # set index values for our pointers
        leftPtr, rightPtr = 0, len(s) - 1

        while leftPtr < rightPtr:
            while leftPtr < rightPtr and not self.alphanumericCheck(s[leftPtr]):
                # move to the next position to skip over non alphanumeric characters
                leftPtr += 1
            while leftPtr < rightPtr and not self.alphanumericCheck(s[rightPtr]):
                rightPtr -= 1
            # check that they are the same character
            if s[leftPtr] != s[rightPtr]:
                return False
            leftPtr += 1
            rightPtr -= 1

        return True

    def alphanumericCheck(self, char):
        ordChar = ord(char)
        if ord("A") <= ordChar <= ord("Z"):
            return True
        elif ord("a") <= ordChar <= ord("z"):
            return True
        elif ord("0") <= ordChar <= ord("9"):
            return True
        else:
            return False
