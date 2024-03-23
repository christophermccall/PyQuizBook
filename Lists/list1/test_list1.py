import unittest
import list1


class List1Test(unittest.TestCase):

    def test_create_list_from_tuple(self):
        test_cases = [
            ((1, 2, 3), [1,2,3]),
            ((1,), [1]),
            ((), []),
            (("foo", "bar"), ["foo", "bar"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.create_list_from_tuple(tt_in))

    def test_drop_last(self):
        test_cases = [
            ([1, 2, 3], [1,2]),
            ([1], []),
            (["foo", "bar"], ["foo"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.drop_last(tt_in))

    def test_drop_first_two(self):
        test_cases = [
            ([1, 2, 3], [3]),
            ([1, 5], []),
            (["foo", "bar", "baz"], ["baz"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.drop_first_two(tt_in))

    def test_drop_mangle(self):
        test_cases = [
            ([1, 2, 3, 4], [3]),
            ([0, 1, 1], []),
            (["foo", "bar", "wow", "baz"], ["wow"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.drop_mangle(tt_in))

    def test_add_item_front(self):
        test_cases = [
            ([1, 2, 3, 4], 3, [3, 1, 2, 3, 4]),
            ([0, 1, 1], 2, [2, 0, 1, 1]),
            (["foo", "bar", "wow", "baz"], "wow", ["wow", "foo", "bar", "wow", "baz"] ),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, list1.add_item_front(tt_in, aaa))

    def test_add_item_end(self):
        test_cases = [
            ([1, 2, 3, 4], 3, [1, 2, 3, 4, 3]),
            ([0, 1, 1], 2, [0, 1, 1, 2]),
            (["foo", "bar", "wow", "baz"], "wow", ["foo", "bar", "wow", "baz", "wow"] ),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, list1.add_item_end(tt_in, aaa))

    def test_add_list_to_list(self):
        test_cases = [
            ([1, 2, 3, 4], [3], [1, 2, 3, 4, 3]),
            ([0, 1, 1], [2], [0, 1, 1, 2]),
            (["foo", "bar", "wow", "baz"], ["wow"], ["foo", "bar", "wow", "baz", "wow"] ),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, list1.add_list_to_list(tt_in, aaa))

# list_and_list_to_tuple
    def test_list_and_list_to_tuple(self):
        test_cases = [
            ([1, 2, 3, 4], [3], ([1, 2, 3, 4], [3])),
            ([0, 1, 1], [2], ([0, 1, 1], [2])),
            (["foo", "bar", "wow", "baz"], ["wow"], (["foo", "bar", "wow", "baz"], ["wow"]) ),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, list1.list_and_list_to_tuple(tt_in, aaa))

# list_and_list_to_list
    def test_list_and_list_to_list(self):
        test_cases = [
            ([1, 2, 3, 4], [3], [[1, 2, 3, 4], [3]]),
            ([0, 1, 1], [2], [[0, 1, 1], [2]]),
            (["foo", "bar", "wow", "baz"], ["wow"], [["foo", "bar", "wow", "baz"], ["wow"]] ),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, list1.list_and_list_to_list(tt_in, aaa))

# create lists
    def test_list_from_range(self):
        test_cases = [
            (5, [0,1,2,3,4]),
            (6, [0,1,2,3,4,5]),
            (0, []),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.list_from_range(tt_in))

    def test_list_from_range2(self):
        test_cases = [
            (0, 5, [0,1,2,3,4]),
            (6, 9, [6,7,8]),
            (17, 23, [17,18,19,20,21,22]),
        ]

        for aaa, bbb, expected in test_cases:
            with self.subTest(f"{aaa} {bbb} -> {expected}"):
                self.assertEqual(expected, list1.list_from_range2(aaa, bbb))

    def test_list_from_range3(self):
        test_cases = [
            (0, 5, [0,1,2,3,4,5]),
            (6, 9, [6,7,8,9]),
            (17, 23, [17,18,19,20,21,22,23]),
        ]

        for aaa, bbb, expected in test_cases:
            with self.subTest(f"{aaa} {bbb} -> {expected}"):
                self.assertEqual(expected, list1.list_from_range3(aaa, bbb))

    def test_list_from_range4(self):
        test_cases = [
            (0, 5, [1,2,3,4,5]),
            (6, 9, [7,8,9]),
            (17, 23, [18,19,20,21,22,23]),
        ]

        for aaa, bbb, expected in test_cases:
            with self.subTest(f"{aaa} {bbb} -> {expected}"):
                self.assertEqual(expected, list1.list_from_range4(aaa, bbb))

    def test_list_from_range_by(self):
        test_cases = [
            (12, 2, [0, 2, 4, 6, 8, 10]),
            (10, 3, [0, 3, 6, 9]),
            (50, 5, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]),
        ]

        for aaa, bbb, expected in test_cases:
            with self.subTest(f"{aaa} {bbb} -> {expected}"):
                self.assertEqual(expected, list1.list_from_range_by(aaa, bbb))

    def test_rev_list(self):
        test_cases = [
            ([1, 2, 3], [3,2,1]),
            ([1], [1]),
            (["foo", "bar"], ["bar", "foo"]),
            ([7, 9, 12, 34, 96, 5, 7, 0], [0, 7, 5, 96, 34, 12, 9, 7]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.rev_list(tt_in))

# concat_list_indexwise
    def test_concat_list_indexwise(self):
        test_cases = [
            ([1, 2, 3, 4], [3, 3, 3, 3], [4,5,6,7]),
            ([2, 1, 1], [2, 1, 8], [4,2,9]),
            (["foo", "bar", "wow", "baz"], ["wow", "bar", "wow", "baz"], ["foowow", "barbar", "wowwow", "bazbaz"]),
            (["M", "na", "i", "Ke"], ["y", "me", "s", "lly"], ['My', 'name', 'is', 'Kelly']),
        ]

        for tt_in, aaa, expected in test_cases:
            with self.subTest(f"{tt_in} {aaa} -> {expected}"):
                self.assertEqual(expected, list1.concat_list_indexwise(tt_in, aaa))

# square_each_item
    def test_square_each_item(self):
        test_cases = [
            ([1, 2, 3], [1,4,9]),
            ([5, 10, 15], [25, 100, 225]),
            ([6, 7], [36, 49]),
            ([7, 9, 12, 34, 96, 5, 7, 0], [49, 81, 144, 1156, 9216, 25, 49, 0]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.square_each_item(tt_in))

#  ["Mike", "", "Emma", "Kelly", "", "Brad"]
    def test_remove_empty_strs(self):
        test_cases = [
            (["", "foo", "bar", "", "wow", "baz"], ["foo", "bar", "wow", "baz"],),
            ([1], [1]),
            (["foo", "bar"], ["foo", "bar"]),
            ([1, 2, 3], [1, 2, 3]),
            ([1, "", 2, 3], [1, 2, 3]),
            (["Mike", "", "Emma", "Kelly", "", "Brad"], ["Mike", "Emma", "Kelly", "Brad"]),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.remove_empty_strs(tt_in))

    def test_remove_item_from(self):
        test_cases = [
            ([0,1,2,3,4,5], 5, [0,1,2,3,4]),
            ([6,7,8,6,9], 6, [7,8,9]),
            ([5, 20, 15, 20, 25, 50, 20], 20, [5, 15, 25, 50]),
        ]

        for aaa, bbb, expected in test_cases:
            with self.subTest(f"{aaa} {bbb} -> {expected}"):
                self.assertEqual(expected, list1.remove_item_from(aaa, bbb))

    def test_leave_item_in(self):
        test_cases = [
            ([0,1,2,3,4,5], 5, [5]),
            ([6,7,8,6,9], 6, [6,6]),
            ([5, 20, 15, 20, 25, 50, 20], 20, [20, 20, 20]),
        ]

        for aaa, bbb, expected in test_cases:
            with self.subTest(f"{aaa} {bbb} -> {expected}"):
                self.assertEqual(expected, list1.leave_item_in(aaa, bbb))

    def test_length_of(self):
        test_cases = [
            ([0,1,2,3,4], 5),
            ([0,1,2,3,4,5], 6),
            ([], 0),
        ]

        for tt_in, expected in test_cases:
            with self.subTest(f"{tt_in} -> {expected}"):
                self.assertEqual(expected, list1.length_of(tt_in))
