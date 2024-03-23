import unittest
import dict1


class Dict1Test(unittest.TestCase):

    def test_create_dict_from_lists(self):
        test_cases = [
            (['a', 'b', 'c', 'd'], [1, 2, 3, 4], {'a': 1, 'b': 2, 'c': 3, 'd': 4}),
            ([0, 1, 1, 2], [2, 0, 1, 1], {0: 2, 1: 1, 2: 1}),
            (["foo", "bar", "wow", "baz"],["wow", "foo", "bar", "wow"], {'bar': 'foo', 'baz': 'wow', 'foo': 'wow', 'wow': 'bar'}),
        ]

        for kkk, vvv, expected in test_cases:
            with self.subTest(f"{kkk} {vvv} -> {expected}"):
                self.assertEqual(expected, dict1.create_dict_from_lists(kkk,vvv))

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
    def test_merge_two_dicts(self):
        test_cases = [
            ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'e': 1, 'f': 2, 'g': 3, 'h': 4}, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 2, 'g': 3, 'h': 4}),
            ({0: 2, 1: 1, 2: 1}, {0: 2, 1: 1, 2: 1}, {0: 2, 1: 1, 2: 1}),
            ({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Forty': 40, 'Fifty': 50}, {'Fifty': 50, 'Forty': 40, 'Ten': 10, 'Thirty': 30, 'Twenty': 20}),
        ]

        for kkk, vvv, expected in test_cases:
            with self.subTest(f"{kkk} {vvv} -> {expected}"):
                self.assertEqual(expected, dict1.merge_two_dicts(kkk,vvv))

# (['Kelly', 'Emma'], {"designation": 'Developer', "salary": 8000}, {})
    def test_init_dict_with_values(self):
        test_cases = [
            (['Kelly', 'Emma'], {"designation": 'Developer', "salary": 8000},
            {'Emma': {'designation': 'Developer', 'salary': 8000}, 'Kelly': {'designation': 'Developer', 'salary': 8000}}),

            (["Honda", "Toyota", "Ford"],{"type": 'Sedan', "engine_size": 1500}, 
            {'Ford': {'engine_size': 1500, 'type': 'Sedan'},
            'Honda': {'engine_size': 1500, 'type': 'Sedan'},
            'Toyota': {'engine_size': 1500, 'type': 'Sedan'}}),

            (["dollars", "yen", "euros"], {'Ten': 10, 'Twenty': 20, 'Thirty': 30},
            {'dollars': {'Ten': 10, 'Thirty': 30, 'Twenty': 20},
            'euros': {'Ten': 10, 'Thirty': 30, 'Twenty': 20},
            'yen': {'Ten': 10, 'Thirty': 30, 'Twenty': 20}}),
        ]

        for kkk, vvv, expected in test_cases:
            with self.subTest(f"{kkk} {vvv} -> {expected}"):
                self.assertEqual(expected, dict1.init_dict_with_values(kkk,vvv))

# careful this test is wonky
    def test_extract_keys_to_dict(self):
        test_cases = [
            (['a', 'c'], {'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'a': 1, 'c': 3}),
            (["name", "salary"], {"name": "Kelly", "age":25, "salary": 8000, "city": "New york" },
            {'name': 'Kelly', 'salary': 8000}),
            ([0, 2], {0: 2, 1: 1, 2: 1}, {0: 2, 2: 1}),
            (["foo", "bar", "baz"], {'bar': 'foo', 'baz': 'wow', 'foo': 'wow', 'wow': 'bar'}, 
            {'bar': 'foo', 'baz': 'wow', 'foo': 'wow'}),
        ]

        for kkk, vvv, expected in test_cases:
            with self.subTest(f"{vvv} {kkk} -> {expected}"):
                self.assertEqual(expected, dict1.extract_keys_to_dict(vvv, kkk))

# careful this test is wonky
    def test_delete_keys_from_dict(self):
        test_cases = [
            (['a', 'c'], {'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'b': 2, 'd': 4}),
            (["name", "salary"], {"name": "Kelly", "age":25, "salary": 8000, "city": "New york" },
            {'age': 25, 'city': 'New york'}),
            ([0, 2], {0: 2, 1: 1, 2: 1}, {1: 1}),
            (["foo", "bar", "baz"], {'bar': 'foo', 'baz': 'wow', 'foo': 'wow', 'wow': 'bar'}, 
            {'wow': 'bar'}),
        ]

        for kkk, vvv, expected in test_cases:
            with self.subTest(f"{vvv} {kkk} -> {expected}"):
                self.assertEqual(expected, dict1.delete_keys_from_dict(vvv, kkk))

    def test_check_dict_for_key(self):
        test_cases = [
            ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 3, True),
            ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 5, False),
            ({"name": "Kelly", "age":25, "salary": 8000, "city": "New York" }, 8000, True),
            ({"name": "Kelly", "age":25, "salary": 8000, "city": "New York" }, "Megan", False),
            ({'bar': 'foo', 'baz': 'wow', 'foo': 'wow', 'wow': 'bar'}, "foo", True),
            ({'bar': 'foo', 'foo': 'wow', 'wow': 'bar'}, "baz", False),
        ]

        for ddd, kkk, expected in test_cases:
            with self.subTest(f"{ddd} {kkk} -> {expected}"):
                self.assertEqual(expected, dict1.check_dict_for_key(ddd, kkk))

    def test_get_key_of_min_value(self):
        test_cases = [
            ({'Physics': 82, 'Math': 65, 'History': 75}, 'Math'),
            ({'Oranges': 12, 'Apples': 7, 'Bananas': 4}, 'Bananas'),
            ({'Foo': 2, 'Bar': 6, 'Baz': 7}, 'Foo'),
        ]

        for ddd, expected in test_cases:
            with self.subTest(f"{ddd} -> {expected}"):
                self.assertEqual(expected, dict1.get_key_of_min_value(ddd))

    def test_get_key_of_max_value(self):
        test_cases = [
            ({'Physics': 82, 'Math': 65, 'History': 75}, "Physics"),
            ({'Oranges': 12, 'Apples': 7, 'Bananas': 4}, "Oranges"),
            ({'Foo': 2, 'Bar': 6, 'Baz': 7}, 'Baz'),
        ]

        for ddd, expected in test_cases:
            with self.subTest(f"{ddd} -> {expected}"):
                self.assertEqual(expected, dict1.get_key_of_max_value(ddd))

