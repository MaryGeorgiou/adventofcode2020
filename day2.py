TOBOGGAN_POLICY = 1
OLD_SLED_RENTAL_POLICY = 2


def parse_password_rule(rule):
    # 15-16 f
    num_range, character = rule.split()
    policy_part_1, policy_part_2 = num_range.split('-')
    return int(policy_part_1), int(policy_part_2), character


def complies_with_other_sled_rental_policy(policy_password):
    rule, password = policy_password.split(": ")
    min_oc, max_oc, character = parse_password_rule(rule)
    char_frequency = password.count(character)
    if min_oc <= char_frequency <= max_oc:
        return True
    return False


def complies_with_toboggan_policy(policy_password):
    rule, password = policy_password.split(": ")
    pos1, pos2, character = parse_password_rule(rule)
    list_of_indexes = find_all_index_positions_of_char(password, character)
    return (pos1 in list_of_indexes and pos2 not in list_of_indexes) or \
           (pos1 not in list_of_indexes and pos2 in list_of_indexes)


def find_all_index_positions_of_char(list_of_chars, char):
    # indexes are stored with base 1
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = list_of_chars.index(char, index_pos)
            index_pos_list.append(index_pos + 1)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list


def sum_of_compliant_passwords(policy_password_list, policy_type=TOBOGGAN_POLICY):
    counter = 0
    policy_check = complies_with_toboggan_policy
    if policy_type == OLD_SLED_RENTAL_POLICY:
        policy_check = complies_with_other_sled_rental_policy
    for policy_password in policy_password_list:
        if policy_check(policy_password):
            counter += 1
    return counter


with open("data/day2.txt") as f:
    data_list = f.readlines()
    print(sum_of_compliant_passwords(data_list))
