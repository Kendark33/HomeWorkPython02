#  Реализуйте алгоритм перемешивания списка.

from random import sample
if __name__ == '__main__':
    nums = range(10)
    l = sample(nums, len(nums))
    print(l)