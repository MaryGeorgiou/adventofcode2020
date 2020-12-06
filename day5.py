def load_data():
    with open("data/day5.txt") as f:
        data = f.readlines()
    return data


def input_to_seat_id(boarding_pass):
    row = boarding_pass[:7].replace('F', '0').replace('B', '1')
    column = boarding_pass[7:].replace('L', '0').replace('R', '1')
    row = int(row, 2)
    column = int(column, 2)
    return row * 8 + column


def data_to_list_of_seat_ids():
    boarding_passes = load_data()
    list_seat_ids = []
    for boarding_pass in boarding_passes:
        seat_id = input_to_seat_id(boarding_pass)
        list_seat_ids.append(seat_id)
    return list_seat_ids


def find_my_seat(list_seat_ids):
    list_seat_ids.sort()
    sum_of_current_seat_ids = sum(list_seat_ids)
    sum_of_seat_ids_if_mine_was_there = sum(list(range(list_seat_ids[0], list_seat_ids[-1] + 1)))
    return sum_of_seat_ids_if_mine_was_there - sum_of_current_seat_ids


seats = data_to_list_of_seat_ids()
print(max(seats))
print(find_my_seat(seats))
