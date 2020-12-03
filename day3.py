def load_data():
    data = []
    with open("data/day3.txt") as f:
        data_list = f.readlines()
        for line in data_list:
            line = [char for char in line]
            data.append(line[:-1])
    return data


def get_one_step_down_the_slope(data_array, row, column_position, steps_right, steps_down):
    row_size = len(data_array[0])
    position_diff = row_size - column_position
    if row_size - column_position > steps_right:
        new_column_position = column_position + steps_right
    else:
        new_column_position = steps_right - position_diff
    return row+steps_down, new_column_position


def count_trees(data_array, steps_right, steps_down):
    column = 0
    row = 0
    tree_counter = 0
    while row < len(data_array)-1:
        new_row, new_column = get_one_step_down_the_slope(data_array, row, column, steps_right, steps_down)
        if data_array[new_row][new_column] == '#':
            tree_counter += 1
        row = new_row
        column = new_column
    return tree_counter


slopes = load_data()
slope = count_trees(slopes, 3, 1)
