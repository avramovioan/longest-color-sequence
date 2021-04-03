import copy, sys, argparse, pathlib

def main():

    test_cases = extract_args()
    for test in test_cases:
        file = open("..\\tests\\{}".format(test), 'r')
        dimensions = file.readline()
        x = get_x(dimensions)
        y = get_y(dimensions)
        arr = get_array_from_file(file)
        length = longest_sequence(arr, x, y)
        file.close()
        print(length)

def extract_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=pathlib.Path, nargs=argparse.ONE_OR_MORE, help='Enter test files.')
    return parser.parse_args().files

def get_array_from_file(file):
    all_lines = file.readlines()
    arr = []
    i = 0
    while i < len(all_lines):
        arr.append(list(all_lines[i].replace(" ", "").strip()))
        i += 1
    return arr


def get_x(dimensions): return int(dimensions.split(' ')[0])
def get_y(dimensions): return int(dimensions.split(' ')[1])

def longest_sequence(array, x, y):
    sequence_length = 0
    curr_sequence_length = 0
    check_array = get_checking_array(array)
    queue = []
    current_char = ''
    i = 0
    while i < x:
        j = 0
        while j < y:
            if check_array[i][j] == False and len(queue) == 0:
                sequence_length = update_sequence_length(curr_sequence_length, sequence_length)
                curr_sequence_length = 0
                current_char = array[i][j]
                position = [i, j]
                queue.append(position)
            curr_sequence_length = go_through_queue(queue,x,y,current_char,check_array,array, curr_sequence_length)
            j+=1
        i+=1
    sequence_length = update_sequence_length(curr_sequence_length, sequence_length)
    return sequence_length

def update_sequence_length(curr_seq_len, sequence_len):
    if curr_seq_len > sequence_len:
        return curr_seq_len
    return sequence_len

def go_through_queue(queue, x, y, curr_char, check_arr, arr, curr_sequence_length):
    while len(queue) > 0:
        curr_pos_x = queue[0][0]
        curr_pos_y = queue[0][1]

        check_arr[curr_pos_x][curr_pos_y] = True
        curr_sequence_length += 1

        # check top
        if check_adjacent('top', x, y, curr_pos_x, curr_pos_y, curr_char, check_arr, arr):
            position = [curr_pos_x - 1, curr_pos_y]
            if not position in queue:
                queue.append(position)

        # check right
        if check_adjacent('right', x, y, curr_pos_x, curr_pos_y, curr_char, check_arr, arr):
            position = [curr_pos_x, curr_pos_y + 1]
            if not position in queue:
                queue.append(position)

        # check bottom
        if check_adjacent('bottom', x, y, curr_pos_x, curr_pos_y, curr_char, check_arr, arr):
            position = [curr_pos_x + 1, curr_pos_y]
            if not position in queue:
                queue.append(position)

        # check left
        if check_adjacent('left', x, y, curr_pos_x, curr_pos_y, curr_char, check_arr, arr):
            position = [curr_pos_x, curr_pos_y - 1]
            if not position in queue:
                queue.append(position)
        queue.pop(0)
    return curr_sequence_length


def check_adjacent(checking_position, x, y, pos_x, pos_y, current_char, check_arr, arr):
    positions= {
        'top': check_top,
        'bottom': check_bottom,
        'right': check_right,
        'left': check_left,
    }
    return positions.get(checking_position)(x,y,pos_x,pos_y, arr, current_char, check_arr)


def check_top(x, y, pos_x, pos_y, arr, current_char, check_arr):
    if pos_x - 1 >= 0 and arr[pos_x - 1][pos_y] == current_char and check_arr[pos_x - 1][pos_y] is False:
        return True
    return False


def check_right(x, y, pos_x, pos_y, arr, current_char, check_arr):
    if pos_y + 1 < y and arr[pos_x][pos_y + 1] == current_char and check_arr[pos_x][pos_y + 1] is False:
        return True
    return False


def check_left(x, y, pos_x, pos_y, arr, current_char, check_arr):
    if pos_y - 1 >= 0 and arr[pos_x][pos_y - 1] == current_char and check_arr[pos_x][pos_y - 1] is False:
        return True
    return False


def check_bottom(x, y, pos_x, pos_y, arr, current_char, check_arr):
    if pos_x + 1 < x and arr[pos_x + 1][pos_y] == current_char and check_arr[pos_x + 1][pos_y] is False:
        return True
    return False


def get_checking_array(arr):
    checking_arr = copy.deepcopy(arr)
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]):
          #  print("{} {}".format(i, j))
            checking_arr[i][j] = False
            j += 1
        i += 1
    return checking_arr


main()