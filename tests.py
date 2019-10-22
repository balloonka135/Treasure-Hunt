import func_task
import oop_task


class TestClass:
    expected_output = [11, 55, 15, 21, 44, 32, 13, 25, 43]

    def test_func_task(self):
        input_array = [[55, 14, 25, 52, 21],
                       [44, 31, 11, 53, 43],
                       [24, 13, 45, 12, 34],
                       [42, 22, 43, 32, 41],
                       [51, 23, 33, 54, 15]]
        traverse_arr = func_task.init_traversal_array()
        result_arr = []

        result = func_task.treasure_traversal(
            0, 0, input_array, traverse_arr, result_arr
        )

        assert result == self.expected_output

    def test_oop_task(self):
        t = oop_task.TreasureHunt()
        t.input_array = [[55, 14, 25, 52, 21],
                         [44, 31, 11, 53, 43],
                         [24, 13, 45, 12, 34],
                         [42, 22, 43, 32, 41],
                         [51, 23, 33, 54, 15]]
        result = t.treasure_traversal()
        assert result == self.expected_output
