# crackme-py

## Description

[crackme.py](./crackme.py)

## Hints

(None)

## How To

First thing when scanning through the file we see our encrypted secret message labeled as ```bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN" ```. There is already a decrypt method setup for us labeled `decode_secret()`, adding a simple method call passing our variable with the flag into the code.
'decode_secret(bezos_cc_secret)'
I also removed the call for `choose_greatest()' which leaves the python code with errors if you try to run it.

## Flag
picoCTF{1|\/|_4_p34|\|ut_dd2c4616}
