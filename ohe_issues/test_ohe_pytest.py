import pytest
from one_hot_encoder import fit_transform


def test_empty():
    """
        TypeError exception test
    """
    with pytest.raises(TypeError):
        fit_transform()


def test_ohe_list():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    exp_size = len(set(cities))

    tranformed_cities = fit_transform(cities)

    assert exp_transformed_cities == tranformed_cities

    unique_cities = set([x[0] for x in tranformed_cities])
    assert 'NY' not in unique_cities

    got_size = len(exp_transformed_cities[0][1])
    assert exp_size == got_size


def test_ohe_args():
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]

    transformed_cities = fit_transform(
        'Moscow', 'New York', 'Moscow', 'London')

    assert exp_transformed_cities == transformed_cities
