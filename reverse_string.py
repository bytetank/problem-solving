"""

Given a string of alphabets and symbols, reverse the character of string such that
only alphabets gets reversed while special character position remains same

e.g.
ab-cd --> dc-ab
pqrst-u!! --> utsrq-p!!

"""


class Solution:

    def rev(self, string: str) -> str:
        string = list(string)
        left_ptr = 0
        right_ptr = len(string) - 1
        while left_ptr < right_ptr:
            if string[left_ptr].isalpha() and string[right_ptr].isalpha():
                string[left_ptr], string[right_ptr] = string[right_ptr], string[left_ptr]
                left_ptr += 1
                right_ptr -= 1
            elif not string[left_ptr].isalpha():
                left_ptr += 1
            elif not string[right_ptr].isalpha():
                right_ptr -= 1
        return "".join(string)

if __name__ == "__main__":
    soln = Solution()

    print(soln.rev("a!!!b.c.d,e'f,ghi"))



    