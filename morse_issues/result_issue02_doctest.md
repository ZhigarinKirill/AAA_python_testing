py -m pytest -v --doctest-modules
============================= test session starts =============================
platform win32 -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- C:\Users\zhiga\AppData\Local\Programs\Python\Python39\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues, configfile: pytest.ini
plugins: anyio-3.4.0
collecting ... collected 4 items

morse.py::morse.encode FAILED                                            [ 25%]
test_morse.py::test_decode[-] PASSED                                     [ 50%]
test_morse.py::test_decode[... --- ...-SOS] PASSED                       [ 75%]
test_morse.py::test_decode[.- .- .-   .--. -.-- - .... --- -.-AAA PYTHON] FAILED [100%]

================================== FAILURES ===================================
___________________________ [doctest] morse.encode ____________________________
034     '... --- ...'
035     >>> encode(message='HELP')
036     '.... . .-.. .--.'
037     >>> encode(message='HELP US WE ARE INSIDE') #doctest: +ELLIPSIS
038         '.... . .-.. .--.  ...  .. -. ... .. -.. .'
039     >>> encode(message='HELP US! WE ARE INSIDE') #doctest: +ELLIPSIS
040     Traceback (most recent call last):
041         ...
042     KeyError: '!'
043     >>> encode(message='HELP US, WE ARE INSIDE')
UNEXPECTED EXCEPTION: KeyError(',')
Traceback (most recent call last):
  File "C:\Users\zhiga\AppData\Local\Programs\Python\Python39\lib\doctest.py", line 1334, in __run
    exec(compile(example.source, filename, "single",
  File "<doctest morse.encode[5]>", line 1, in <module>
  File "C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues\morse.py", line 46, in encode
    encoded_signs = [
  File "C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues\morse.py", line 47, in <listcomp>
    LETTER_TO_MORSE[letter] for letter in message
KeyError: ','
C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues\morse.py:43: UnexpectedException
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
FAILED morse.py::morse.encode
FAILED test_morse.py::test_decode[.- .- .-   .--. -.-- - .... --- -.-AAA PYTHON]
========================= 2 failed, 2 passed in 0.07s =========================
