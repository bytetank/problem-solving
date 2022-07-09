"""
Given a list of 1s and 0s shift all 0s to left
"""



class ShiftZeros:

    def __init__(self, input_list):
        self.input_list = input_list

    def shift_zero_left(self):
        sum = 0
        for elem in self.input_list:
            sum += elem
        for i in range(len(self.input_list)):
            if i < len(self.input_list) - sum:
                self.input_list[i] = 0
            else:
                self.input_list[i] = 1

s = ShiftZeros([1, 1, 0, 1, 1])
s.shift_zero_left()
print(s.input_list)