import pytest
from one_hot_encoder import fit_transform


def test_empty():
    """
        TypeError exception test
    """
    with pytest.raises(TypeError):
        fit_transform()


def test_ohe01():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert exp_transformed_cities == fit_transform(cities)


def test_ohe02():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    tranformed_cities = fit_transform(cities)
    unique_cities = set([x[0] for x in tranformed_cities])
    assert 'NY' not in unique_cities


def test_vect_size():
    """
        Vector size test
    """
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_size = len(set(cities))
    transformed_cities = fit_transform(cities)
    got_size = len(transformed_cities[0][1])
    assert exp_size == got_size
