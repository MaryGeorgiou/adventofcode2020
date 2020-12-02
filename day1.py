def find_pair_that_adds_to_sum(list_of_nums, goal_sum):
    hashset = set()
    for num in list_of_nums:
        diff = goal_sum - num
        if diff in hashset:
            return num, diff
        else:
            hashset.add(num)
    return None


def find_triple_that_adds_to_sum(list_of_nums, goal_sum):
    for i in range(len(list_of_nums)):
        diff = goal_sum - list_of_nums[i]
        pair = find_pair_that_adds_to_sum(list_of_nums[i + 1:], diff)
        if pair is not None:
            num1, num2 = pair
            return list_of_nums[i], num1, num2
