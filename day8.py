def load_data():
    with open('data/day8.txt') as f:
        entries = f.read().splitlines()
    return [(entry, 0) for entry in entries]


def read_command(str_command):
    command, argument = str_command.split(' ')
    return command, int(argument)


def flip_command(command):
    # if command is jmp turns it to nop and vice versa
    if 'nop' in command:
        return 'jmp ' + command.split(' ')[1], 0
    else:
        return 'nop ' + command.split(' ')[1], 0


def execute_command(str_command, current_index, accumulator_value):
    command, argument = read_command(str_command)
    if command == 'nop':
        return accumulator_value, current_index + 1
    elif command == 'acc':
        return accumulator_value + argument, current_index + 1
    elif command == 'jmp':
        return accumulator_value, current_index + argument
    else:
        print(f"Command {command} does not exist")


def find_accumulator_value(instructions):
    second_time = False
    index = 0
    accumulator_value = 0
    while not second_time and index < len(instructions):
        new_command, times_executed = instructions[index]
        if times_executed >= 1:
            return accumulator_value
        new_accumulator_value, new_index = execute_command(new_command, index, accumulator_value)
        instructions[index] = (new_command, times_executed + 1)
        accumulator_value = new_accumulator_value
        index = new_index
    return accumulator_value


def command_creates_infinite_loop(instructions, index_of_erratic_command):
    command, _ = instructions[index_of_erratic_command]
    instructions[index_of_erratic_command] = flip_command(command)
    index = 0
    acc = 0
    is_finished = False
    while not is_finished:
        new_command, times_executed = instructions[index]
        if times_executed >= 1:
            return True
        acc, new_index = execute_command(new_command, index, acc)
        instructions[index] = (new_command, times_executed + 1)
        index = new_index
        if new_index >= len(instructions):
            is_finished = True
    return False


def correct_instructions():
    # the erratic command should be in the commands already executed
    # until one command gets executed a second time.
    instructions = load_data()
    second_time = False
    index = 0
    accumulator_value = 0
    jmp_nop_commands_executed = []
    while not second_time:
        new_command, times_executed = instructions[index]
        if 'nop' in new_command or 'jmp' in new_command:
            jmp_nop_commands_executed.append((new_command, index))
        if times_executed >= 1:
            break
        new_accumulator_value, new_index = execute_command(new_command, index, accumulator_value)
        instructions[index] = (new_command, times_executed + 1)
        accumulator_value = new_accumulator_value
        index = new_index

    for command in jmp_nop_commands_executed:
        command_index = command[1]
        command_create_inf_loop = command_creates_infinite_loop(load_data(), command_index)
        if not command_create_inf_loop:
            instructions = load_data()
            instructions[command_index] = flip_command(instructions[command_index][0])
            return instructions


# part1
print(find_accumulator_value(load_data()))
# part2
print(find_accumulator_value(correct_instructions()))
