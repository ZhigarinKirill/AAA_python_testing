import unittest
from one_hot_encoder import fit_transform


class TestOHE(unittest.TestCase):
    def test_empty(self):
        """
            TypeError exception test
        """
        self.assertRaises(TypeError, fit_transform)

    def test_ohe01(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(exp_transformed_cities, fit_transform(cities))

    def test_ohe02(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        tranformed_cities = fit_transform(cities)
        unique_cities = set([x[0] for x in tranformed_cities])
        self.assertNotIn('NY', unique_cities)

    def test_vect_size(self):
        """
            Vector size test
        """
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_size = len(set(cities))
        transformed_cities = fit_transform(cities)
        got_size = len(transformed_cities[0][1])
        self.assertTrue(exp_size == got_size)
