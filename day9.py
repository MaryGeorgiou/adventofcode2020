def load_data():
    with open('data/day9.txt') as f:
        entries = f.read().splitlines()
    return [int(entry) for entry in entries]


def slide_over_data(number_list, window=5):
    for i in range(len(number_list)):
        result = number_list[i:i + window]
        yield i + window, result


def pair_that_adds_us_to_number(list_of_nums, number):
    hashset = set()
    for num in list_of_nums:
        diff = number - num
        if diff in hashset:
            return num, diff
        else:
            hashset.add(num)
    return None


def find_contiguous_set_that_adds_to_number(goal_sum):
    list_of_nums = load_data()
    window = 3
    not_found = True
    while not_found:
        slide = slide_over_data(list_of_nums, window)
        not_found_inner = True
        while not_found_inner:
            _, window_of_nums = next(slide)
            if sum(window_of_nums) == goal_sum:
                return window_of_nums
            if len(window_of_nums) < window:
                not_found_inner = False
        window += 1
        if window == len(list_of_nums):
            not_found = False


def first_num_in_sequence_that_does_not_belong(window):
    numbers = load_data()
    slide = slide_over_data(numbers, window)
    finished = False
    while not finished:
        i, window_of_nums = next(slide)
        if pair_that_adds_us_to_number(window_of_nums, numbers[i]) is None:
            return numbers[i]
        if len(window_of_nums) < window:
            finished = True


# part1
print(first_num_in_sequence_that_does_not_belong(25))
# part2
set_of_nums = find_contiguous_set_that_adds_to_number(167829540)
print(max(set_of_nums) + min(set_of_nums))
