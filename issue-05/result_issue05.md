py -m pytest -v --cov
 
============================= test session starts =============================

platform win32 -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- C:\Users\zhiga\AppData\Local\Programs\Python\Python39\python.exe

cachedir: .pytest_cache
rootdir: C:\Users\zhiga\Documents\AAA\Python\Tests\HW\issue-05
plugins: anyio-3.4.0, cov-3.0.0
collecting ... collected 3 items

test_issue05.py::test_what_is_year_now_exception PASSED                  [ 33%]

test_issue05.py::test_what_is_year_now_YMD PASSED                        [ 66%]

test_issue05.py::test_what_is_year_now_DMY PASSED                        [100%]


----------- coverage: platform win32, python 3.9.9-final-0 -----------
Name              Stmts   Miss  Cover
-------------------------------------
issue05.py           20      0   100%
test_issue05.py      18      0   100%
-------------------------------------
TOTAL                38      0   100%


============================== 3 passed in 1.54s ==============================
