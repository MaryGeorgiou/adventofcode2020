def load_data():
    with open('data/day10.txt') as f:
        entries = f.read().splitlines()
    return [int(entry) for entry in entries]


def find_diffs_in_chain_of_adapters(adapters):
    diff_1 = 0
    diff_2 = 0
    diff_3 = 1  # there's always the diff of 3 jolts of the built-in adapter.
    for i in range(len(adapters) - 1):
        difference = adapters[i + 1] - adapters[i]
        if difference == 1:
            diff_1 += 1
        elif difference == 2:
            diff_2 += 1
        elif difference == 3:
            diff_3 += 1
        else:
            return None
    return diff_1, diff_2, diff_3


def find_possible_path_rec(current_number, adapters):
    max_adapter = max(adapters)
    if current_number == max_adapter or current_number not in adapters:
        return 0
    if max_adapter - current_number <= 3:
        increment = 1
    else:
        increment = 0
    if current_number in possible_paths.keys():
        return possible_paths[current_number]

    total = find_possible_path_rec(current_number + 1, adapters) + \
            find_possible_path_rec(current_number + 2, adapters) + \
            find_possible_path_rec(current_number + 3, adapters) + \
            increment

    possible_paths[current_number + 1] = find_possible_path_rec(current_number + 1, adapters)
    possible_paths[current_number + 2] = find_possible_path_rec(current_number + 2, adapters)
    possible_paths[current_number + 3] = find_possible_path_rec(current_number + 3, adapters)
    return total


adapters = load_data()
adapters.sort()
adapters.insert(0, 0)

# part1
print(find_diffs_in_chain_of_adapters(adapters))

# part 2
possible_paths = {}
print(find_possible_path_rec(0, adapters))
