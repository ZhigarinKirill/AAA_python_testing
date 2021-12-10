from unittest.mock import patch
from issue05 import what_is_year_now
import pytest
from urllib import request
import io


def test_what_is_year_now_exception():
    data = io.StringIO('{"currentDateTime": "2021:11:27T18:21Z"}')
    with patch.object(request, 'urlopen', return_value=data):
        with pytest.raises(ValueError):
            _ = what_is_year_now()


def test_what_is_year_now_empty_year():
    data = io.StringIO('{"currentDateTime": "?-11-27T18:21Z"}')
    with patch.object(request, 'urlopen', return_value=data):
        with pytest.raises(ValueError):
            _ = what_is_year_now()


def test_what_is_year_now_YMD():
    exp_year = 2021
    data = io.StringIO('{"currentDateTime": "2021-11-27T18:21Z"}')
    with patch.object(request, 'urlopen', return_value=data):
        year = what_is_year_now()
    assert exp_year == year


def test_what_is_year_now_DMY():
    exp_year = 2021
    data = io.StringIO('{"currentDateTime": "01.03.2021T18:21Z"}')
    with patch.object(request, 'urlopen', return_value=data):
        year = what_is_year_now()
    assert exp_year == year
