py -m pytest -v
============================= test session starts =============================
platform win32 -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- C:\Users\zhiga\AppData\Local\Programs\Python\Python39\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues, configfile: pytest.ini
plugins: anyio-3.4.0
collecting ... collected 3 items

test_morse.py::test_decode[-] PASSED                                     [ 33%]
test_morse.py::test_decode[... --- ...-SOS] PASSED                       [ 66%]
test_morse.py::test_decode[.- .- .-   .--. -.-- - .... --- -.-AAA PYTHON] FAILED [100%]

================================== FAILURES ===================================
_________ test_decode[.- .- .-   .--. -.-- - .... --- -.-AAA PYTHON] __________

s = '.- .- .-   .--. -.-- - .... --- -.', exp = 'AAA PYTHON'

    @pytest.mark.parametrize('s, exp', [
        ('', ''),
        ('... --- ...', 'SOS'),
        ('.- .- .-   .--. -.-- - .... --- -.', 'AAA PYTHON')
    ])
    def test_decode(s, exp):
>       assert decode(s) == exp
E       AssertionError: assert 'AAAPYTHON' == 'AAA PYTHON'
E         - AAA PYTHON
E         ?    -
E         + AAAPYTHON

test_morse.py:11: AssertionError
=========================== short test summary info ===========================
FAILED test_morse.py::test_decode[.- .- .-   .--. -.-- - .... --- -.-AAA PYTHON]
========================= 1 failed, 2 passed in 0.05s =========================
