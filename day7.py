from collections import defaultdict


def load_data():
    with open("data/day7.txt") as f:
        return f.readlines()


def get_data_from_line(entry):
    bag_color, contents = entry.split(" bags contain ")
    if 'contain no other bags' in entry:
        return bag_color, []
    contents = contents.split(', ')
    parsed_contents = []
    for bag in contents:
        bag_data = bag.split(' ')
        amount = int(bag_data[0])
        color = ' '.join(bag_data[1:3])
        parsed_contents.append((color, amount))
    return bag_color, parsed_contents


def get_color_pairs_from_line(entry):
    bag_color_outer, contents = entry.split(" bags contain ")
    if 'contain no other bags' in entry:
        return None
    contents = contents.split(', ')
    parsed_contents = []
    for bag in contents:
        bag_data = bag.split(' ')
        color_inner = ' '.join(bag_data[1:3])
        parsed_contents.append((color_inner, bag_color_outer))
    return parsed_contents


def load_data_in_inverse_dictionary():
    data = load_data()
    bag_tuples = []
    for entry in data:
        color_tuples = get_color_pairs_from_line(entry)
        if color_tuples is not None:
            bag_tuples = bag_tuples + color_tuples
    bags = defaultdict(list)
    for color, bag_color_outer in bag_tuples:
        bags[color].append(bag_color_outer)
    return bags


def load_data_in_dictionary():
    data = load_data()
    bags = {}
    for entry in data:
        bag_color, bag_contents = get_data_from_line(entry)
        bags[bag_color] = bag_contents
    return bags


def bags_that_can_contain_input_color(color):
    bags = load_data_in_inverse_dictionary()
    if color not in bags.keys():
        return "Color does not exist in data"
    bags_visited = []
    bags_to_visit = [color]
    while bags_to_visit:
        now_checking_color = bags_to_visit.pop(0)
        neighbour_bags = bags[now_checking_color]
        for neighbour_bag_color in neighbour_bags:
            bags_to_visit.append(neighbour_bag_color)
        bags_visited.append(now_checking_color)
    bags_visited.remove(color)
    return set(bags_visited)


def number_of_bags_in_bag(color, bags):
    count = 0
    if color not in bags.keys():
        return "Color does not exist in data"
    for bag_content in bags[color]:
        color, amount = bag_content
        count += amount
        count += number_of_bags_in_bag(color, bags) * amount
    return count


# part 1
print(len(bags_that_can_contain_input_color('shiny gold')))

# part2
bags_dict = load_data_in_dictionary()
print(number_of_bags_in_bag('shiny gold', bags_dict))
