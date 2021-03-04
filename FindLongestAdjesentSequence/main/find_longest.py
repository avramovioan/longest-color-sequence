import copy, sys

def main():

    test_cases = list(sys.argv)
    test_cases.pop(0)
    print(test_cases)
    for test in test_cases:
        file = open("..\\tests\\{}".format(test), 'r')
        dimentios = file.readline()
        x = int(dimentios.split(' ')[0])
        y = int(dimentios.split(' ')[1])
        all_lines = file.readlines()
        arr = []
        i = 0
        while i < len(all_lines):
            arr.append(list(all_lines[i].replace(" ","").strip()))
            i += 1
        # print(arr)
        # print(x)
        # print(y)
        length = longest_sequence(arr, x, y)
        print(length)

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
                if curr_sequence_length > sequence_length:
                    sequence_length = curr_sequence_length
                curr_sequence_length = 0
                current_char = array[i][j]
                position = [i, j]
                queue.append(position)
            while len(queue) > 0:
                curr_pos_x = queue[0][0]
                curr_pos_y = queue[0][1]

                check_array[curr_pos_x][curr_pos_y] = True
                curr_sequence_length += 1

                # check top
                if curr_pos_x - 1 >= 0 and array[curr_pos_x - 1][curr_pos_y] == current_char and check_array[curr_pos_x - 1][curr_pos_y] is False:
                    position = [curr_pos_x - 1, curr_pos_y]
                    if not position in queue:
                        queue.append(position)

                # check right
                if curr_pos_y + 1 < y and array[curr_pos_x][curr_pos_y + 1] == current_char and check_array[curr_pos_x][curr_pos_y + 1] is False:
                    position = [curr_pos_x, curr_pos_y + 1]
                    if not position in queue:
                        queue.append(position)

                # check bottom
                if curr_pos_x + 1 < x and array[curr_pos_x + 1][curr_pos_y] == current_char and check_array[curr_pos_x + 1][curr_pos_y] is False:
                    position = [curr_pos_x + 1, curr_pos_y]
                    if not position in queue:
                        queue.append(position)

                # check left
                if curr_pos_y - 1 >= 0 and array[curr_pos_x][curr_pos_y - 1] == current_char and check_array[curr_pos_x][curr_pos_y - 1] is False:
                    position = [curr_pos_x, curr_pos_y - 1]
                    if not position in queue:
                        queue.append(position)
                queue.pop(0)
            j+=1
        i+=1

    if curr_sequence_length > sequence_length:
        sequence_length = curr_sequence_length
    return sequence_length


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

# TEST CASES
# arrayInput1 = [["R", "R", "B"],
#                ["G", "G", "R"],
#                ["R", "B", "G"]]
#
# x = 6
# y = 6
# arrayInput2 = [["R", "R", "R", "G"],
#                ["G", "B", "R", "G"],
#                ["R", "G", "G", "G"],
#                ["G", "G", "B", "B"]]
#
# arrayInput3 = [["R", "R", "B", "B", "B", "B"],
#                ["B", "R", "B", "B", "G", "B"],
#                ["B", "G", "G", "B", "R", "B"],
#                ["B", "B", "R", "B", "G", "B"],
#                ["R", "B", "R", "B", "R", "B"],
#                ["R", "B", "B", "B", "G", "B"]]
#
# arrayInput4 = []
# i = 0
# while i < x:
#     curr_arr = []
#     j = 0
#     while j < y:
#         curr_arr.append("R")
#         j += 1
#     arrayInput4.append(curr_arr)
#     i += 1
