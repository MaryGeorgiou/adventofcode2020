from collections import Counter


def read_data():
    with open('data/day6.txt') as f:
        data = f.read()
    group_answers = data.split('\n\n')
    return group_answers


def get_unique_answers_for_group(group_answers):
    return Counter(group_answers.replace('\n', ''))


def get_intersection_of_answers_for_group(group_answers):
    member_answers = group_answers.split('\n')
    return set.intersection(*map(set, member_answers))


def get_sum_of_unique_answers():
    sum_of_unique_answers = 0
    groups_answers = read_data()
    for answers in groups_answers:
        unique_answers = len(get_unique_answers_for_group(answers))
        sum_of_unique_answers += unique_answers
    return sum_of_unique_answers


def get_sum_of_intersection_of_answers_per_group():
    sum_of_common_answers = 0
    groups_answers = read_data()
    for answers in groups_answers:
        common_answers = len(get_intersection_of_answers_for_group(answers))
        sum_of_common_answers += common_answers
    return sum_of_common_answers


print(get_sum_of_unique_answers())
print(get_sum_of_intersection_of_answers_per_group())
