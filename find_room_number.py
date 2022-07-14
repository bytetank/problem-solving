"""
Find the room number from the given sequence number by ignoring the room numbers containing 2 in it.
"""


class Solution:

    def __init__(self, skip_room):
        self.skip_room = str(skip_room)


    def get_room_number(self, actual_room):
        counter = 0
        for i in range(actual_room):
            counter += 1
            while str(counter).find(self.skip_room) != -1:
                counter += 1
        return counter


if __name__ == "__main__":
    soln = Solution(2)
    print(soln.get_room_number(20))
