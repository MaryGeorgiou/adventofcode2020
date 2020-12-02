def parse_password_rule(rule):
    # 15-16 f
    num_range, character = rule.split()
    min_occurrences, max_occurrences = num_range.split('-')
    return int(min_occurrences), int(max_occurrences), character


def complies_with_policy(policy_password):
    rule, password = policy_password.split(": ")
    min_oc, max_oc, character = parse_password_rule(rule)
    char_frequency = password.count(character)
    if min_oc <= char_frequency <= max_oc:
        return True
    return False


def sum_of_non_compliant_passwords(policy_password_list):
    counter = 0
    for policy_password in policy_password_list:
        if complies_with_policy(policy_password):
            counter += 1
    return counter


with open("data/day2.txt") as f:
    data_list = f.readlines()
    print(sum_of_non_compliant_passwords(data_list))
