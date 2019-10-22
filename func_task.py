""" Functional way of implementing treasure hunting """


def input_data():
    array = []
    for i in range(5):
        input_arr = input().split()
        input_arr = [int(i) for i in input_arr]
        array.append(input_arr)
    return array


def init_traversal_array():
    traverse_arr = []
    for i in range(5):
        n = []
        for i in range(5):
            n.append(False)
        traverse_arr.append(n)
    return traverse_arr


def treasure_traversal(i, j, input_array, traverse_arr, result_arr):
    if not traverse_arr[i][j]:
        result_arr.append(int('{0}{1}'.format(str(i + 1), str(j + 1))))
        traverse_arr[i][j] = True
        n = input_array[i][j]
        a = n // 10
        b = n % 10
        if i + 1 == a and j + 1 == b:
            return result_arr
        i = a - 1
        j = b - 1

    return treasure_traversal(i, j, input_array, traverse_arr, result_arr)


if __name__ == '__main__':
    array = input_data()
    traverse_arr = init_traversal_array()
    result_arr = []

    treasure_traversal(0, 0, array, traverse_arr, result_arr)
