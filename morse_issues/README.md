1. Enter the following command in the console to run doctest
    ```
    py -m doctest -v -o NORMALIZE_WHITESPACE <path to morse.py>
    ```
2. Enter the following command in the console to run pytest parametrize tests
    ```
    py -m pytest -v <path to dir with tests or to test_morse.py>
    ```
3. Enter the following command in the console to run pytest with doctest
    ```
    py -m pytest -v --doctest-modules <path to dir with tests>
    ```    