from unittest.mock import patch
from issue05 import what_is_year_now
import pytest
import json


def test_what_is_year_now_exception():
    with patch.object(json, 'loads',
                      return_value={'currentDateTime': '2021:11:27T18:21Z'}):
        with pytest.raises(ValueError):
            _ = what_is_year_now()


def test_what_is_year_now_YMD():
    exp_year = 2021
    with patch.object(json, 'loads',
                      return_value={'currentDateTime': '2021-11-27T18:21Z'}):
        year = what_is_year_now()
    assert exp_year == year


def test_what_is_year_now_DMY():
    exp_year = 2021
    with patch.object(json, 'loads',
                      return_value={'currentDateTime': '01.03.2021T18:21Z'}):
        year = what_is_year_now()
    assert exp_year == year
