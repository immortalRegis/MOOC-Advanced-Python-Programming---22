# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, wk_num: int, correct_nums : list):
        self.__week_num = wk_num
        self.__correct_nums = correct_nums
    
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__correct_nums])

    def hits_in_place(self, numbers):
        return [number if number in self.__correct_nums else -1 for number in numbers ]

