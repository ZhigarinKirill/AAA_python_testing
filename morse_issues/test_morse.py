import pytest
from morse import decode


@pytest.mark.parametrize('s, exp', [
    ('', ''),
    ('... --- ...', 'SOS'),
    ('.- .- .-   .--. -.-- - .... --- -.', 'AAA PYTHON')
])
def test_decode(s, exp):
    assert decode(s) == exp
