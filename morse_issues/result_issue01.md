py -m doctest -v -o NORMALIZE_WHITESPACE morse.py
 
Trying:
    encode(message='')
Expecting:
    ''
ok

Trying:
    encode(message='SOS') 
Expecting:
    '... --- ...'
ok

Trying:
    encode(message='HELP')
Expecting:
    '.... . .-.. .--.'
ok

Trying:
    encode(message='HELP US WE ARE INSIDE') #doctest: +ELLIPSIS
Expecting:
        '.... . .-.. .--.  ...  .. -. ... .. -.. .'
ok

Trying:
    encode(message='HELP US! WE ARE INSIDE') #doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: '!'
ok

Trying:
    encode(message='HELP US, WE ARE INSIDE')
Expecting:
    '.... . .-.. .--.   ..- ... --..--   .-- .   .- .-. .   .. -. ... .. -.. .'
**********************************************************************
File "C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues\morse.py", line 43, in morse.encode
Failed example:
    encode(message='HELP US, WE ARE INSIDE')
Exception raised:
    Traceback (most recent call last):
      File "C:\Users\zhiga\AppData\Local\Programs\Python\Python39\lib\doctest.py", line 1334, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest morse.encode[5]>", line 1, in <module>
        encode(message='HELP US, WE ARE INSIDE')
      File "C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues\morse.py", line 46, in encode
        encoded_signs = [
      File "C:\Users\zhiga\Documents\AAA\Python\Tests\HW\morse_issues\morse.py", line 47, in <listcomp>
        LETTER_TO_MORSE[letter] for letter in message
    KeyError: ','
2 items had no tests:
    morse
    morse.decode
**********************************************************************
1 items had failures:
   1 of   6 in morse.encode
6 tests in 3 items.
5 passed and 1 failed.
***Test Failed*** 1 failures.
