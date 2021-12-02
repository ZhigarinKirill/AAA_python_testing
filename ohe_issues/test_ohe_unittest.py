import unittest
from one_hot_encoder import fit_transform


class TestOHE(unittest.TestCase):
    def test_empty(self):
        """
            TypeError exception test
        """
        self.assertRaises(TypeError, fit_transform)

    def test_ohe_list(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        exp_size = len(set(cities))

        transformed_cities = fit_transform(cities)

        self.assertEqual(exp_transformed_cities, transformed_cities)

        unique_cities = set([x[0] for x in transformed_cities])
        self.assertNotIn('NY', unique_cities)

        got_size = len(transformed_cities[0][1])
        self.assertTrue(exp_size == got_size)

    def test_ohe_args(self):
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        transformed_cities = fit_transform(
            'Moscow', 'New York', 'Moscow', 'London')

        self.assertEqual(exp_transformed_cities, transformed_cities)
