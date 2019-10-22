""" OOP way for treasure hunting """


class TreasureHunt:

    def __init__(self, array=[]):
        self.input_array = array

    def input_array_data(self):
        for i in range(5):
            input_arr = input().split()
            input_arr = [int(i) for i in input_arr]
            self.input_array.append(input_arr)

    def init_traversal_array(self):
        traverse_arr = []
        for i in range(5):
            n = []
            for i in range(5):
                n.append(False)
            traverse_arr.append(n)
        return traverse_arr

    def treasure_traversal(self):
        i = 0
        j = 0

        traverse_arr = self.init_traversal_array()
        result_arr = []

        while not traverse_arr[i][j]:
            result_arr.append('{0}{1}'.format(str(i + 1), str(j + 1)))
            traverse_arr[i][j] = True
            n = self.input_array[i][j]
            a = n // 10
            b = n % 10
            if i + 1 == a and j + 1 == b:
                return list(map(int, result_arr))
            i = a - 1
            j = b - 1


if __name__ == '__main__':
    t = TreasureHunt()
    t.input_array_data()
    t.treasure_traversal()










